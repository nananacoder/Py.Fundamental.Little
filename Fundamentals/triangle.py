#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
判断三个数值是否可以构成三角形
'''
while True:
    s = raw_input("Please input 3 integers to combine a triangle(enter q to quit):")
    S = s.split(',')
    if s == 'q':
        break
    else:
        a = int(S[0])
        b = int(S[1])
        c = int(S[2])
        if a+b > c and a+c > b  and b+c > a:
            if a == b and b == c:
                print "It's a regular triangle."
            else:
                if a == b or b == c or a == c:
                    print "It's an isosceles triangle."
                else:
                    print "It's a normal triangle."
        else:
            print "sorry, the 3 numbers cannot combine a triangle."

    print 'The end'
