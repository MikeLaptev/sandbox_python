import threading
import multiprocessing
from threading import Thread


def target(**kwargs):
    process_name = multiprocessing.current_process().name
    thread_name = threading.current_thread().name
    print(f"p:{process_name} - t:{thread_name}: {kwargs['data']}")


if __name__ == "__main__":
    pool = [
        Thread(target=target, name=f"simple-thread-{idx}", kwargs={"data": "boom"})
        for idx in range(10)
    ]

    for x in pool:
        x.start()
    for x in pool:
        x.join()
