#!/usr/bin/env python
# -*-coding:utf-8-*-

from threading import Thread
from time import sleep


class AAA(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.message = "Hello Parallel!!"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Thread Starting.\n")
        x = 0
        while x<10:
            self.print_message()
            sleep(2)
            x += 1

        print("Thread End\n")

if __name__ == '__main__':
    print ("Process Start\n")
    hello_python = AAA()
    hello_python.start()
    print ("Process End.\n")