import multiprocessing
import threading
from multiprocessing import Process


def target(**kwargs):
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    print(f"p:{process_name} - t:{thread_name}: {kwargs['data']}")


if __name__ == "__main__":
    # NOTE: for multiprocessing - data that's passed around - should be pickable, so, relatively ease one
    pool = [
        Process(target=target, name=f"simple-process-{idx}", kwargs={"data": "boom"})
        for idx in range(10)
    ]

    for x in pool:
        x.start()
    for x in pool:
        x.join()
