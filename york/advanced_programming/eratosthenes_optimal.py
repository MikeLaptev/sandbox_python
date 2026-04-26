"""
Sieve of Eratosthenes — parallel segmented implementation.

Key ideas:
  - A plain sieve (is_prime array) is used for the small 'seed' primes up to sqrt(n).
  - The remaining range [sqrt(n)+1, n] is split into equal segments.
  - Each segment is sieved independently using only the seed primes.
  - multiprocessing.Pool (not threading) is used so workers bypass the GIL.
  - For first_n_primes, Rosser's theorem gives a tight upper bound that almost
    always avoids a second sieve pass.
"""

import math
from multiprocessing import Pool


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _simple_sieve(limit: int) -> list[int]:
    """Classic Sieve of Eratosthenes for all primes up to `limit` (inclusive).

    This is only called once to produce the 'seed' primes up to sqrt(upper_bound).
    """
    if limit < 2:
        return []

    # bytearray is more memory-efficient than list[bool] or list[int]
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[0] = is_prime[1] = 0  # 0 and 1 are not prime by definition

    # Only iterate up to sqrt(limit) — any composite above it has a factor below it
    for p in range(2, math.isqrt(limit) + 1):
        if is_prime[p]:
            # Start at p^2 — all smaller multiples were already crossed off
            # by the prime factors of those multiples.
            # Slice assignment is a single C-level memset, much faster than a Python loop.
            is_prime[p * p :: p] = bytearray(len(range(p * p, limit + 1, p)))

    return [i for i, flag in enumerate(is_prime) if flag]


def _sieve_segment(args: tuple[int, int, list[int]]) -> list[int]:
    """Sieve one segment [start, end] using precomputed seed primes.

    Called by each worker process. The segment's local array is tiny (chunk_size
    bytes), so memory stays manageable regardless of the overall upper bound.

    args is a tuple so Pool.map can pass a single argument per worker.
    """
    start, end, seed_primes = args

    # Local boolean array: index `i` represents the number `(start + i)`
    is_prime = bytearray([1]) * (end - start + 1)

    for p in seed_primes:
        # Ceiling division to find the first multiple of p that is >= start.
        # Using integer arithmetic avoids float rounding: ceil(start/p)*p
        first_multiple = ((start + p - 1) // p) * p

        # Never mark p itself composite (matters when the segment starts at or below p)
        if first_multiple == p:
            first_multiple += p

        if first_multiple > end:
            continue  # p has no multiples in this segment

        # Cross off every multiple of p in [first_multiple, end]
        is_prime[first_multiple - start :: p] = bytearray(
            len(range(first_multiple, end + 1, p))
        )

    return [start + i for i, flag in enumerate(is_prime) if flag]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def primes_up_to(n: int, workers: int = 4) -> list[int]:
    """Return a sorted list of all prime numbers <= n.

    Uses a parallel segmented sieve:
      1. Compute seed primes up to sqrt(n) on the main process.
      2. Split `(sqrt(n), n]` into `workers` equal segments.
      3. Sieve each segment in a separate OS process (true CPU parallelism).
      4. Concatenate seed primes + results in order.

    For small n the overhead of multiprocessing dominates; the function is still
    correct but a plain sieve would be faster in that regime.
    """
    if n < 2:
        return []

    sqrt_n = math.isqrt(n)
    # Step 1: cheap single-process sieve for the seed range
    seed_primes = _simple_sieve(sqrt_n)

    # Edge case: entire range fits within the seed sieve
    if n <= sqrt_n:
        return seed_primes

    # Step 2: partition (sqrt_n, n] into at most `workers` non-empty segments.
    # Ceiling division ensures the last element is always included.
    range_start = sqrt_n + 1
    total = n - range_start + 1
    chunk_size = max(1, math.ceil(total / workers))  # never zero

    segments: list[tuple[int, int, list[int]]] = []
    for i in range(workers):
        seg_start = range_start + i * chunk_size
        if seg_start > n:
            break  # fewer chunks needed than workers — that's fine
        seg_end = min(seg_start + chunk_size - 1, n)
        segments.append((seg_start, seg_end, seed_primes))

    # Step 3: parallel sieve — each process gets its own memory space, no GIL
    with Pool(processes=len(segments)) as pool:
        results = pool.map(_sieve_segment, segments)

    # Step 4: merge — seed_primes is already sorted; segments are in order
    primes = seed_primes
    for segment_primes in results:
        primes.extend(segment_primes)
    return primes


def first_n_primes(n: int, workers: int = 4) -> list[int]:
    """Return the first `n` prime numbers.

    Strategy: use Rosser's theorem to estimate a tight upper bound for the n-th prime,
    sieve once, and slice.  The estimate is tight enough that a second pass is almost
    never needed.

    Rosser's theorem (1941): for n >= 6,  p_n < n * (ln n + ln(ln n))
    We add a small integer margin to be safe for edge cases near n=6.
    """
    if n <= 0:
        return []

    # Avoid log(0) / log(log(n)) domain errors for tiny n
    if n == 1:
        return [2]

    if n < 6:
        # The formula is only tight for n >= 6; just sieve a safe small range
        return _simple_sieve(15)[:n]

    # Rosser upper bound for the n-th prime + safety margin
    ln_n = math.log(n)
    upper_bound = int(n * (ln_n + math.log(ln_n))) + 3

    primes = primes_up_to(upper_bound, workers=workers)

    # The estimate is conservative enough that this loop almost never executes.
    # When it does (very small n or numerical edge cases), extend from the previous
    # endpoint rather than re-sieving from scratch.
    while len(primes) < n:
        new_upper = upper_bound * 2
        # Only sieve the new range we haven't covered yet
        extra = primes_up_to(new_upper, workers=workers)
        primes = extra          # simpler than extending; primes_up_to is idempotent
        upper_bound = new_upper

    return primes[:n]


# ---------------------------------------------------------------------------
# Smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    actual_till_n = primes_up_to(100)
    expected_till_n = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    ]
    print(f"{actual_till_n   = }")
    print(f"{expected_till_n = }")
    assert actual_till_n == expected_till_n, "primes_up_to(100) failed"

    actual_first_n = first_n_primes(95)
    expected_first_n = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
        223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
        293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379,
        383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
        463, 467, 479, 487, 491, 499,
    ]
    print(f"{actual_first_n   = }")
    print(f"{expected_first_n = }")
    assert actual_first_n == expected_first_n, "first_n_primes(95) failed"

    print("All assertions passed.")
