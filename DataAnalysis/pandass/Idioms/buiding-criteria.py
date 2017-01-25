#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame({"AAA":[4,5,6,7], "BBB":[10,20,30,40], "CCC":[100,50,-30,-50]})
# print (df)
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   20   50
# 2    6   30  -30
# 3    7   40  -50


# Select with multi-column criteria

# without assignment returns a Series

newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= 40), 'AAA'] #返回 BBB小于25并且CCC大于40的对应AAA的值
# print (newseries)

# 0    4
# 1    5
# Name: AAA, dtype: int64

newseries1 = df.loc[(df['BBB'] > 25) & (df['CCC'] >= 40), 'AAA']
# print (newseries1)
#返回:
# Series([], Name: AAA, dtype: int64)


#with assignment modifies the DataFrame.)
df.loc[(df['BBB'] >25) | (df['CCC'] >75), 'AAA'] = -1 # 改变df本身的值,将BBB>25对应AAA的值 或者 CCC>75对应AAA的值变为-1
print (df)
#
#     AAA  BBB  CCC
# 0   -1   10  100
# 1    5   20   50
# 2   -1   30  -30
# 3   -1   40  -50


#Select rows with data closest to certain value using argsort
#根据离某个具体数值最近的要求,对某列进行排序
df = pd.DataFrame({"AAA":[4,5,6,7], "BBB":[10,20,30,40], "CCC":[100,50,-30,-50]})

aValue = 43.0
sort_df = df.ix[(df.CCC-aValue).abs().argsort()]
# print (sort_df)
#
#     AAA  BBB  CCC
# 1    5   20   50
# 0    4   10  100
# 2    6   30  -30
# 3    7   40  -50


# Dynamically reduce a list of criteria using a binary operators
df = pd.DataFrame({"AAA":[4,5,6,7], "BBB":[10,20,30,40], "CCC":[100,50,-30,-50]})
crit1 = df.AAA <= 5.5
crit2 = df.BBB == 10.0
crit3 = df.CCC > -40.0
AllCrit = crit1 & crit2 & crit3

crit_df = df[AllCrit]
print (crit_df)
#     AAA  BBB  CCC
# 0    4   10  100


