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
    """doing it at first the hard way"""
    # threads = list()
    # for index in range(3):
    #     logging.info(f'Main    : create and start thread {index}.')
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()
    #
    # for index, thread in enumerate(threads):
    #     logging.info(f'Main    : before joining thread {index}')
    #     thread.join()
    #     logging.info(f'Main    : thread {index} done')

    '''doing it with more clean and OK way to start them at the same time'''
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(thread_function, range(40))
