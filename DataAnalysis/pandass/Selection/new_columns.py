#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Efficiently and dynamically creating new columns using applymap
http://stackoverflow.com/questions/16575868/efficiently-creating-additional-columns-in-a-pandas-dataframe-using-map
"""


df = pd.DataFrame({'AAA':[1,2,1,3], 'BBB':[1,1,2,2], 'CCC':[2,1,3,1]})
#     AAA  BBB  CCC
# 0    1    1    2
# 1    2    1    1
# 2    1    2    3
# 3    3    2    1

source_cols = df.columns
new_cols = [str(x)+'_cat' for x in source_cols]

categories = {1: 'Alpha', 2: 'Beta', 3: 'Charlie' }
df[new_cols] = df[source_cols].applymap(categories.get)
#将旧数据和新数据点关系用字典categories表示出来.将旧列中的每个元素通过applymap中的函数 影射到字典中对应的value,赋给新列.
print (df)


"""
Keep other columns when using min() with groupby
"""

df = pd.DataFrame({'AAA' : [1,1,1,2,2,2,3,3], 'BBB' : [2,1,3,4,5,1,2,3]})
#    AAA  BBB
# 0    1    2
# 1    1    1
# 2    1    3
# 3    2    4
# 4    2    5
# 5    2    1
# 6    3    2
# 7    3    3


#方法1: idxmin() to get the index of the mins
grp_df = df.loc[df.groupby("AAA")["BBB"].idxmin()]
print (grp_df)
#     AAA  BBB
# 1    1    1
# 5    2    1
# 6    3    2


#方法2: sort then take first of each
grp_df2 = df.sort_values(by="BBB").groupby("AAA", as_index=False).first()
print (grp_df2)
#    AAA  BBB
# 0    1    1
# 1    2    1
# 2    3    2


#Notice the same results, with the exception of the index.