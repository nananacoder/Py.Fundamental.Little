'''
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array:


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],[10,-65]
[0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14],[8,-50]
[1],[1,0]
[-1],[0,-1]
[0,0,0,0,0,0,0,0,0],[0,0]
[],[]
'''

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        pos_count = 0
        neg = 0
        for e in arr:
            if e <= 0:
                neg += e
            elif e > 0:
                pos_count += 1
        return [pos_count, neg]


def count_positives_sum_negatives2(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

def count_positives_sum_negatives3(arr):
    return [sum([1 for i in arr if i > 0]), sum([i for i in arr if i<0])] if arr else []

