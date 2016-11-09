#!/usr/bin/env python
# -*- coding:utf-8 -*-

import numpy

def numpysum(n):
    a = numpy.arange(n) ** 2
    b = numpy.arange(n) ** 3
    c = a + b
    return c

n = input('please give me an n value:')
c = numpysum(n)
print c

