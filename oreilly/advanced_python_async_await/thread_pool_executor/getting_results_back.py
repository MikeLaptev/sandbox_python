import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor


def target(*args):
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    data: str = args[0]["data"]
    print(f"p:{process_name} - t:{thread_name}: {data}")

    return " <--> ".join([data, data[::-1]])


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(target, [{"data": f"boom + {idx}"} for idx in range(10)])
        print(f"{[*results] = }")
