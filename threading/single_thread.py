import concurrent.futures
import time
import threading
import logging


def thread_function(name):
    logging.info(f'Thread {name} is starting')
    time.sleep(3)
    logging.info(f'Thread {name} is finishing')


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(
        format=format,
        level=logging.INFO,
        datefmt="%H:%M:%S"
    )

    # this was the single threaded version
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")
