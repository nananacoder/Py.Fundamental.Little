#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# Using both row labels and value conditionals

df = pd.DataFrame({'AAA':[4,5,6,7], 'BBB':[10,20,30,40], 'CCC':[100,50,-30,-50]})
# print (df)
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   20   50
# 2    6   30  -30
# 3    7   40  -50

new_df = df[(df.AAA <= 6) & (df.index.isin([0,2,4]))] # AAA中值小于6 同时index必须是0,2,4中的索引数
# print (new_df)
#      AAA  BBB  CCC
# 0    4   10  100
# 2    6   30  -30


# Use loc for label-oriented slicing and iloc positional slicing
data = {'AAA':[4,5,6,7], 'BBB':[10,20,30,40], 'CCC':[100,50,-30,-50]}
df = pd.DataFrame(data,index=['foo','bar','boo','kar']) #改变index
print (df)
#    AAA  BBB  CCC
# foo    4   10  100
# bar    5   20   50
# boo    6   30  -30
# kar    7   40  -50


#切片方法
#There are 2 explicit slicing methods, with a third general case
# 1. Positional-oriented (Python slicing style : exclusive of end)
# 2. Label-oriented (Non-Python slicing style : inclusive of end)
# 3. General (Either slicing style : depends on if the slice contains labels or positions)


#Label
print (df.loc['bar':'kar'])
#返回 bar到kar所有 行
#      AAA  BBB  CCC
# bar    5   20   50
# boo    6   30  -30
# kar    7   40  -50

#Generic
print (df.ix[0:3]) # same as iloc.[0:3]
#      AAA  BBB  CCC
# foo    4   10  100
# bar    5   20   50
# boo    6   30  -30

print (df.ix['bar':'kar']) #Same as .loc['bar':'kar']
#     AAA  BBB  CCC
# bar    5   20   50
# boo    6   30  -30
# kar    7   40  -50



# Ambiguity arises when an index consists of integers with a non-zero start or non-unit increment.
# 当索引名字为数字时,就会在label,和loc中产生歧义.
df2 = pd.DataFrame(data=data,index=[1,2,3,4])

#Position-oriented
print (df2.iloc[1:3]) # 忽略第0行,取第1行和第2行
#    AAA  BBB  CCC
# 2    5   20   50
# 3    6   30  -30

#Label_oriented
print (df2.loc[1:3]) # 取标签名字为1 到标签名字为3 中间所有的行
#    AAA  BBB  CCC
# 1    4   10  100
# 2    5   20   50
# 3    6   30  -30

#Generic-oriented
print (df2.ix[1:3]) #Generic情况下,采用label-oriented,取标签名字,结果是df2.loc[1:3]
# AAA  BBB  CCC
# 1    4   10  100
# 2    5   20   50
# 3    6   30  -30

print (df2.ix[0:3]) #Generic情况下,采用position-oriented,取位置索引值,结果是df2.iloc[0:3],因为df2.loc[0:3]会引发KeyError
#    AAA  BBB  CCC
# 1    4   10  100
# 2    5   20   50
# 3    6   30  -30


"""Using inverse operator (~) to take the complement of a mask
   用逆算符~ 来得到给定条件相反的结果
"""
df = pd.DataFrame({'AAA':[4,5,6,7], 'BBB':[10,20,30,40], 'CCC':[100,50,-30,-50]})

iv_df = df[~((df.AAA <=6) & df.index.isin([0,2,4]))]
print (iv_df)
#     AAA  BBB  CCC
# 1    5   20   50
# 3    7   40  -50