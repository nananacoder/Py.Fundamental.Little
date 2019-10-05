#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from multiprocessing.dummy import Pool as ThreadPool

deal_lst = ['....%d...' % i for i in range(1000)]


def deal_func(tup):
    index = tup[0]
    content = tup[1]
    print index, content

if __name__ == '__main__':
    pool = ThreadPool(4)
    results = pool.map(deal_func, enumerate(deal_lst))
    pool.close()
    pool.join()