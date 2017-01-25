#!/usr/bin/python3.5
# -*- coding: utf-8 -*-


#http://stackoverflow.com/questions/14957116/how-to-split-a-dataframe-according-to-a-boolean-criterion

import pandas as pd
import numpy as np

df = pd.DataFrame({'AAA':[4,5,6,7], 'BBB':[10,20,30,40], 'CCC':[100,50,-30,-50]})
# print (df)
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   20   50
# 2    6   30  -30
# 3    7   40  -50

#按条件分割
dflow = df[df.AAA <= 5]  # AAA中值小于5对应行取出来.
# print (dflow)
#
#     AAA  BBB  CCC
# 0    4   10  100
# 1    5   20   50

dfhigh = df[df.AAA > 5]
print (dfhigh)

#     AAA  BBB  CCC
# 2    6   30  -30
# 3    7   40  -50
