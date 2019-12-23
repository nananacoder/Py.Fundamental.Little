#!/usr/bin/local/python
# -*- coding: utf-8 -*-

# https://www.hackerrank.com/challenges/nested-list/forum

def test1():
    score_set = set()
    l1 = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append([name, score])
        score_set.add(score)

    res_score = sorted(list(score_set))[1]
    return '\n'.join([name for name, score in l1 if score == res_score])


def test2():
    # more pythonic style
    l1 = [[input(), float(input())]for _ in range(int(input()))]
    print(l1)
    score_lst = [s for n, s in l1]
    print(score_lst)
    second_lowest_score = sorted(list(set(score_lst)))[1]
    return '\n'.join([n for n, s in l1 if s == second_lowest_score])


if __name__ == '__main__':
    print(test2())

    for _, i in enumerate(range(5)):
        print(i)


