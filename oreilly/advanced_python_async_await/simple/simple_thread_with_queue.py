import threading
import multiprocessing
from queue import Queue
from threading import Thread


def target(**kwargs):
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    kwargs["queue"].put((process_name, thread_name, kwargs["data"]))
    print(f"p:{process_name} - t:{thread_name}: {kwargs['data']}")


if __name__ == "__main__":
    results = Queue()
    pool = [
        Thread(
            target=target,
            name=f"simple-thread-{idx}",
            kwargs={"data": f"boom + {idx}", "queue": results},
        )
        for idx in range(10)
    ]

    for x in pool:
        x.start()
    for x in pool:
        x.join()

    while not results.empty():
        print(f"{results.get() = }")
