import threading
import logging


def threading_with(statement):
    with statement:
        print ('%s acquired via with' % statement)

def threading_not_with(statement):
    statement.acquire()
    try:
        print ('%s acquired directly' % statement)
    finally:
        statement.release()

if __name__ == '__main__':

    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)

    threading_synchronization_list = [lock, rlock, condition, mutex]

    for statement in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with, args=(statement,))
        t2 = threading.Thread(target=threading_not_with, args=(statement, ))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

