#!/opt/local/bin/python3
# authon: John Richardson
#   desc: Creates threads on any function.

import threading
from queue import Queue

q = Queue()


def createWorkers(list):
    for worker in list:
        q.put(worker)
    return q


def threader(func):
    while True:
        worker = q.get()
        func(worker)
        q.task_done()


def createThreads(threadCount, func):
    for i in range(threadCount):
        t = threading.Thread(target=threader, args=(func,))
        t.daemon = True
        t.start()


# Drop this to thread a function
def useThreader(list, threadCount, func):
    createWorkers(list)
    createThreads(threadCount, func)
    q.join()
