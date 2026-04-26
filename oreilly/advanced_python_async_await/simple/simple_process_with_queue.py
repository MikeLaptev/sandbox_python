import multiprocessing
import threading
from multiprocessing import Process, Queue


def target(**kwargs):
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    kwargs["queue"].put((process_name, thread_name, kwargs["data"]))
    print(f"p:{process_name} - t:{thread_name}: {kwargs['data']}")


if __name__ == "__main__":
    results = Queue()
    # NOTE: for multiprocessing - data that's passed around - should be pickable, so, relatively ease one
    pool = [
        Process(
            target=target,
            name=f"simple-process-{idx}",
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
