def longest_consec(strarr, k):
    n = len(strarr)
    if k <= 0 or k >= n or n == 0:
        return ""
    else:
        y = strarr[:]
        y.sort(key=len).reverse()
        small_strarr = []
        for i in range(k):
            small_strarr.append(y[i])



        index1 = strarr.index(s1)
        index2 = strarr.index(s2)
        y = [index1, index2]
        y.sort()
        index1 = y[0]
        index2 = y[1]
        result = strarr[index1]+strarr[index2]
        return result

strarr = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
k = 1


print longest_consec(strarr, k)
