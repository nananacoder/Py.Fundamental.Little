#!/usr/bin/env python
# coding=utf-8

'''
Sum of Pairs

Given a list of integers and a single sum value,
return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.


l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

test.describe("Testing For Sum of Pairs")
test.expect(sum_pairs(l1, 8) == [1, 7], "Basic: %s should return [1, 7] for sum = 8" % l1)
test.expect(sum_pairs(l2, -6) == [0, -6], "Negatives: %s should return [0, -6] for sum = -6" % l2)
test.expect(sum_pairs(l3, -7) == None, "No Match: %s should return None for sum = -7" % l3)
test.expect(sum_pairs(l4, 2) == [1, 1], "First Match From Left: %s should return [1, 1] for sum = 2 " % l4)
test.expect(sum_pairs(l5, 10) == [3, 7], "First Match From Left REDUX!: %s should return [3, 7] for sum = 10 " % l5)
test.expect(sum_pairs(l6, 8) == [4, 4], "Duplicates: %s should return [4, 4] for sum = 8" % l6)
test.expect(sum_pairs(l7, 0) == [0, 0], "Zeroes: %s should return [0, 0] for sum = 0" % l7)
test.expect(sum_pairs(l8, 10) == [13, -3], "Subtraction: %s should return [13, -3] for sum = 10" % l8)


其实这是一个很简单的问题。要做的事情是这样的，我们想象面前摆放着一个打乱的纸牌堆，每张牌上都有个数字，
我们要找到两张加起来的值等于50，而且这两张牌要尽量在牌堆的上面(后一张尽量靠上)。
当我们这样解析题目后，问题就变得简单了。按照我们的直觉，我们可以尝试这么做：
从上向下一张一张翻看，翻每一张牌都计算需要什么样的牌和他配对，再查看他之前翻过的牌中是否有可以配对的。这样就可以最快地找到最靠近牌堆上面的配对了！

'''

#
# def sum_pairs(ints, s):
#     length = len(int)
#     list_end = {}
#     i = 0
#     while i < length:
#         if list_end[s - ints[i]]:
#             return [s - ints[i], ints[i]]
#         list_end[ints[i]] = True
#         i += 1

def sum_pairs(ints, s):
    #for i in range(len(ints)):
    list_end = []
    for res in ints:
        m = s - res
        if m in ints:
            list_end.append([res,m])
            ints.remove(res)
    if list_end:
        return list_end



l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

s = 10
print sum_pairs(l5, s)

