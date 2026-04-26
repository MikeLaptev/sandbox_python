import threading
import multiprocessing
import time
from threading import Thread, Lock


def target(a_shared_data, a_lock, a_num_of_iterations):
    ten_percent = a_num_of_iterations / 10
    for i in range(a_num_of_iterations):
        process_name = multiprocessing.current_process().name
        thread_name = threading.current_thread().name
        with a_lock:
            current = a_shared_data["value"]
            time.sleep(0.00001)
            a_shared_data["value"] = current + 1

        # without a look
        """
        current = a_shared_data['value']
        time.sleep(0.00001)
        a_shared_data['value'] = current + 1
        """
        if i % ten_percent == 0:
            print(f"p:{process_name} - t:{thread_name}: {current}")


if __name__ == "__main__":
    num_of_threads = 60
    num_of_iterations = 10_000
    lock = Lock()
    data = {"value": 0}
    pool = [
        Thread(
            target=target,
            name=f"simple-thread-{idx}",
            args=(data, lock, num_of_iterations),
        )
        for idx in range(num_of_threads)
    ]

    for x in pool:
        x.start()
    for x in pool:
        x.join()

    print(f"Final Value without lock: {data['value']}")
    print(f"Lost increments: {num_of_threads * num_of_iterations - data['value']}")
