#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

"""
Performing arithmetic with a multi-index that needs broadcasting
#http://stackoverflow.com/questions/19501510/divide-entire-pandas-multiindex-dataframe-by-dataframe-variable/19502176#19502176
"""

cols = pd.MultiIndex.from_tuples([(x,y) for x in ['A','B','C'] for y in ('O','I')])
print (cols)
# MultiIndex(levels=[[u'A', u'B', u'C'], [u'I', u'O']],
#            labels=[[0, 0, 1, 1, 2, 2], [1, 0, 1, 0, 1, 0]])

df = pd.DataFrame(np.random.rand(2,6), index=['n', 'm'], columns=cols)
print(df)
#           A                   B                   C
#           O         I         O         I         O         I
# n  0.284828  0.993977  0.596545  0.266429  0.208324  0.519463
# m  0.178315  0.048492  0.775625  0.812744  0.476486  0.857532

df = df.div(df['C'], level=1)
print(df)
#           A                   B              C
#           O         I         O         I    O    I
# n  0.225728  1.297872  0.637558  2.222893  1.0  1.0
# m  1.766070  0.701242  0.687128  1.737651  1.0  1.0




