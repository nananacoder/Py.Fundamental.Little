#!/usr/bin/env
# -*-coding:utf-8-*-

import threading
import time


def func(i):
    print ("function called by thread %i\n" % i)
    time.sleep(2)
    print ("thread %i\n" % i)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=func, args=(i,))
    threads.append(t)
    t.start()
    t.join()  # makes the calling thread wait until the thread has finishes the execution.
    print ("for loop %i end" % i)
