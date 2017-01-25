#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.DataFrame({'AAA':[4,5,6,7], 'BBB':[10,20,30,40], 'CCC':[100,50,-30,-50]})
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   20   50
# 2    6   30  -30
# 3    7   40  -50


#if-then/if-then-else on one column

df.ix[df.AAA >= 5, 'BBB'] = -1 # 如果AAA对应的值 大于5, 对应ROW中 BBB的值变成-1

# print (df)
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   -1   50
# 2    6   -1  -30
# 3    7   -1  -50

df.ix[df.AAA >= 5, ['BBB', 'CCC']] = 555
# print (df)
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5  555  555
# 2    6  555  555
# 3    7  555  555

df.ix[df.AAA < 5, ['BBB', 'CCC']] = 2000
# print (df)
#     AAA   BBB   CCC
# 0    4   2000  2000
# 1    5   555   555
# 2    6   555   555
# 3    7   555   555

# 或者设置一个mask来改变df中的部分值
df_mask = pd.DataFrame({'AAA':[True]*4, 'BBB':[False]*4, 'CCC':[True, False]*2})
# print (df_mask)
#    AAA    BBB    CCC
# 0  True  False   True
# 1  True  False  False
# 2  True  False   True
# 3  True  False  False

print (df.where(df_mask, -1000)) # 将df_mask中设为false的对应位置 中的df值改为-1000
# 并不改变原先df中的数据,返回新的DataFrame
#     AAA   BBB   CCC
# 0    4 -1000  2000
# 1    5 -1000 -1000
# 2    6 -1000   555
# 3    7 -1000 -1000


# if-then-else using numpy’s where()
df = pd.DataFrame({'AAA':[4,5,6,7], 'BBB':[10,20,30,40], 'CCC':[100,50,-30,-50]})
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   20   50
# 2    6   30  -30
# 3    7   40  -50


df['logic'] = np.where(df['AAA']>5, 'high', 'low')
#如果AAA中的数据大于5的话,新column:logic中对应同一行中的数据为high,小于等于5,对应数据为low
print (df)
#     AAA  BBB  CCC logic
# 0    4   10  100   low
# 1    5   20   50   low
# 2    6   30  -30  high
# 3    7   40  -50  high


