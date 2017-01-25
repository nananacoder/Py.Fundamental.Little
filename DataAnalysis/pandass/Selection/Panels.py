#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


'''Extend a panel frame by transposing, adding a new dimension, and transposing back to the original dimensions
   三维, 可以理解为DataFrame的容器
'''

rng = pd.date_range('1/1/2013', periods=100, freq='D') #频率是day 2013.1.1到其后100天.
data = np.random.randn(100,4)
cols = ['A','B','C','D']

df1, df2, df3 = pd.DataFrame(data,rng,cols), pd.DataFrame(data,rng,cols), pd.DataFrame(data,rng,cols)
# 每个DataFrame都是一个100row*4columns的二维

pf = pd.Panel({'df1':df1, 'df2':df2, 'df3':df3})
print (pf)
# <class 'pandas.core.panel.Panel'>
# Dimensions: 3 (items) x 100 (major_axis) x 4 (minor_axis)
# Items axis: df1 to df3
# Major_axis axis: 2013-01-01 00:00:00 to 2013-04-10 00:00:00
# Minor_axis axis: A to D


#Assignment using Transpose

#pandas版本<1.5时 Minor_axis 添加'E'
pf = pf.transpose(2,0,1)
pf['E'] = pd.DataFrame(data, rng, cols)
pf = pf.transpose(1,2,0)
print (pf)
# <class 'pandas.core.panel.Panel'>
# Dimensions: 3 (items) x 100 (major_axis) x 5 (minor_axis)
# Items axis: df1 to df3
# Major_axis axis: 2013-01-01 00:00:00 to 2013-04-10 00:00:00
# Minor_axis axis: A to E

#新版本>1.5 可以直接添加
pf.loc[:,:,'F'] = pd.DataFrame(data, rng, cols)
print (pf)
# <class 'pandas.core.panel.Panel'>
# Dimensions: 3 (items) x 100 (major_axis) x 6 (minor_axis)
# Items axis: df1 to df3
# Major_axis axis: 2013-01-01 00:00:00 to 2013-04-10 00:00:00
# Minor_axis axis: A to F


# Mask a panel by using np.where and then reconstructing the panel with the new masked values
# http://stackoverflow.com/questions/14650341/boolean-mask-in-pandas-panel