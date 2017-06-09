#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Starting %s \n" % name)
    time.sleep(3)
    print ("Exiting %s \n"  % name)

if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='background_process',target=foo)
    process_with_name.daemon = True # to execute the process in background
    NO_process_with_name = multiprocessing.Process(name='NO_backgound_process',target=foo)
    NO_process_with_name.daemon = False

    process_with_name.start()
    NO_process_with_name.start()