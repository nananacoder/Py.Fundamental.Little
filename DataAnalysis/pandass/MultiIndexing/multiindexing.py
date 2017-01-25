#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Creating a multi-index from a labeled frame
http://stackoverflow.com/questions/14916358/reshaping-dataframes-in-pandas-based-on-column-labels
"""

df = pd.DataFrame({
    'row': [0,1,2],
    'One_X': [1.1,1.1,1.1],
    'One_Y': [1.2,1.2,1.2],
    'Two_X': [1.11,1.11,1.11],
    'Two_Y': [1.22,1.22,1.22]
})
#     One_X  One_Y  Two_X  Two_Y  row
# 0    1.1    1.2   1.11   1.22    0
# 1    1.1    1.2   1.11   1.22    1
# 2    1.1    1.2   1.11   1.22    2

# As Labelled Index
df = df.set_index('row')
# print (df)
#        One_X  One_Y  Two_X  Two_Y
# row
# 0      1.1    1.2   1.11   1.22
# 1      1.1    1.2   1.11   1.22
# 2      1.1    1.2   1.11   1.22


## With Hierarchical Columns
df.columns = pd.MultiIndex.from_tuples([tuple(c.split('_')) for c in df.columns])
print (df)
#        One        Two
#        X    Y     X     Y
# row
# 0    1.1  1.2  1.11  1.22
# 1    1.1  1.2  1.11  1.22
# 2    1.1  1.2  1.11  1.22
print (df.columns)
# MultiIndex(levels=[['One', 'Two'], ['X', 'Y']],
#            labels=[[0, 0, 1, 1], [0, 1, 0, 1]])


## Now stack & Reset
df = df.stack(0).reset_index(1)
print (df)
#     level_1     X     Y
# row
# 0       One  1.10  1.20
# 0       Two  1.11  1.22
# 1       One  1.10  1.20
# 1       Two  1.11  1.22
# 2       One  1.10  1.20
# 2       Two  1.11  1.22

## And fix the labels (Notice the label 'level_1' got added automatically)
df.columns = ['Sample', 'ALL_X', 'ALL_Y']
print (df)
#      Sample  ALL_X  ALL_Y
# row
# 0      One   1.10   1.20
# 0      Two   1.11   1.22
# 1      One   1.10   1.20
# 1      Two   1.11   1.22
# 2      One   1.10   1.20
# 2      Two   1.11   1.22

