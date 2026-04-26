import math
from collections import defaultdict
from functools import reduce
from typing import List


class XORAfterRangeMultiplicationQueriesI:

    def xor_after_queries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7

        for query in queries:
            l, r, k, v = query
            v %= mod
            i: int = l
            while i <= r and i < len(nums):
                nums[i] *= v
                nums[i] %= mod
                i += k

        r: int = nums[0]
        for i in range(1, len(nums)):
            r ^= nums[i]

        return r

    def xor_after_queries_opt(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        note: no idea what's behind this solution, but want to try it out
        """
        mod: int = 10**9 + 7
        n: int = len(nums)

        updates = defaultdict(lambda: defaultdict(list))

        for l, r, k, v in queries:
            rem = l % k
            start = (l - rem) // k
            end = (r - rem) // k
            updates[k][rem].append((start, end, v))

        mult = [1] * n

        for k in updates:
            for rem in updates[k]:
                size = (n - rem + k - 1) // k
                diff = [1] * (size + 1)

                for s, e, v in updates[k][rem]:
                    diff[s] = diff[s] * v % mod
                    if e + 1 < len(diff):
                        diff[e + 1] = diff[e + 1] * pow(v, mod - 2, mod) % mod

                cur = 1
                for i in range(size):
                    cur = cur * diff[i] % mod
                    idx = rem + i * k
                    if idx < n:
                        mult[idx] = mult[idx] * cur % mod

        for i in range(n):
            nums[i] = nums[i] * mult[i] % mod

        ans = 0
        for x in nums:
            ans ^= x

        return ans

    def xor_after_queries_opt_opt(
        self, nums: List[int], queries: List[List[int]]
    ) -> int:
        """
        note: no idea what's behind this solution as well, but want to try it out
        """
        mod: int = 10**9 + 7
        n: int = len(nums)

        b = int(math.sqrt(n)) + 1

        small = defaultdict(list)
        inverse = {}

        for l, r, k, v in queries:
            if k >= b:
                for i in range(l, r + 1, k):
                    nums[i] = (nums[i] * v) % mod
            else:
                small[k].append((l, r, v))

        factors = [1] * n

        for k, qlist in small.items():
            events = [[] for _ in range(k)]
            for l, r, v in qlist:
                res = l % k
                step = (r - l) // k
                last = l + step * k

                events[res].append((l, v))  # start multiplying by v
                end_idx = last + k
                if end_idx < n:  # place an end marker if inside array
                    if v in inverse:
                        inv_v = inverse[v]
                    else:
                        inv_v = pow(v, mod - 2, mod)
                        inverse[v] = inv_v
                    events[res].append((end_idx, inv_v))

            for res in range(k):
                ev = events[res]
                if not ev:
                    continue
                ev.sort()  # sort by index
                cur = 1
                ptr = 0
                m = len(ev)
                i = res
                while i < n:
                    while ptr < m and ev[ptr][0] == i:
                        cur = (cur * ev[ptr][1]) % mod
                        ptr += 1
                    factors[i] = (factors[i] * cur) % mod
                    i += k

        for i in range(n):
            nums[i] = (nums[i] * factors[i]) % mod

        ans = 0
        for num in nums:
            ans ^= num
        return ans
