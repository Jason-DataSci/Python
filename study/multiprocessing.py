# Process
import os
from multiprocessing import Process, current_process

def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc_name = current_process().name
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc_name))

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    proc = Process(target=doubler, name='Test', args=(2,))
    proc.start()
    procs.append(proc)

    for proc in procs:
        proc.join()

# Logger
import logging
import multiprocessing
import os
from multiprocessing import Process, Lock

def printer(item, lock):
    """
    Prints out the item that was passed in
    """
    lock.acquire()
    try:
        print((item + 1) ** 10 )
    finally:
        lock.release()

if __name__ == '__main__':
    lock = Lock()
    items = range(5, 9)
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    for item in items:
        p = Process(target=printer, args=(item, lock))
        p.start()

# Pool
from multiprocessing import Pool

def doubler(number):
    return number * 2

if __name__ == '__main__':
    numbers = [5, 10, 20]
    pool = Pool(processes=3)
    print(pool.map(doubler, numbers))


from multiprocessing import Pool

def doubler(number):
    return number * 2

if __name__ == '__main__':
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))

# Queue
from multiprocessing import Process, Queue

sentinel = -1

def creator(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:

        q.put(item)


def my_consumer(q):
    """
    Consumes some data and works on it

    In this case, all it does is double the input
    """
    while True:
        data = q.get()
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)

        if data is sentinel:
            break


if __name__ == '__main__':
    q = Queue()
    data = [5, 10, 13, -1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))
    process_one.start()
    process_two.start()

    q.close()
    q.join_thread()

    process_one.join()
    process_two.join()


def main():
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool()
    cpus = multiprocessing.cpu_count()
    results = []
    for i in xrange(0, cpus):
        result = pool.apply_async(task, args=(i,))
        results.append(result)
    pool.close()
    pool.join()
    for result in results:
        print(result.get())
