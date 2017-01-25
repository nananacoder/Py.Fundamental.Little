#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import itertools

"""Slicing a multi-index with xs
http://stackoverflow.com/questions/12590131/how-to-slice-multindex-columns-in-pandas-dataframes
"""
coords = [('AA','one'),('AA','six'),('BB','one'),('BB','two'),('BB','six')]
index = pd.MultiIndex.from_tuples(coords)

df = pd.DataFrame([11,22,33,44,55], index=index, columns=['MyData'])
print(df)
#          MyData
# AA one      11
#    six      22
# BB one      33
#    two      44
#    six      55


#To take the cross section of the 1st level and 1st axis the index:
B_df = df.xs("BB", level=0,axis=0)
print(B_df)
#         MyData
# one      33
# two      44
# six      55

# ...and now the 2nd level of the 1st axis.(第二层优先级的索引)
six_df = df.xs("six", level=1, axis=0)
print(six_df)
#      MyData
# AA      22
# BB      55



#Slicing a multi-index with xs, method #2
#http://stackoverflow.com/questions/14964493/multiindex-based-indexing-in-pandas
index = list(itertools.product(['Ada', 'Quinn', 'Violet'], ['Comp', 'Math', 'Sci']))
headr = list(itertools.product(['Exams', 'Labs'], ['I', 'II']))

indx = pd.MultiIndex.from_tuples(index, names=['Stuent', 'Course'])
cols = pd.MultiIndex.from_tuples(headr)

data = [[70+x+y+(x*y)%3 for x in range(4)] for y in range(9)]

df = pd.DataFrame(data,index=indx, columns=cols)
print(df)

#                   Exams     Labs
#                   I  II    I  II
# Stuent Course
# Ada    Comp      70  71   72  73
#        Math      71  73   75  74
#        Sci       72  75   75  75
# Quinn  Comp      73  74   75  76
#        Math      74  76   78  77
#        Sci       75  78   78  78
# Violet Comp      76  77   78  79
#        Math      77  79   81  80
#        Sci       78  81   81  81


ALL = slice(None)
violet_df = df.loc['Violet']
print(violet_df)
#            Exams     Lab
#            I  II    I  II
# Course
# Comp      76  77   78  79
# Math      77  79   81  80
# Sci       78  81   81  81

math_df = df.loc[(ALL, 'Math'), ALL]
print(math_df)
#                    Exams     Lab
#                   I  II    I  II
# Stuent Course
# Ada    Math      71  73   75  74
# Quinn  Math      74  76   78  77
# Violet Math      77  79   81  80

math_2 = df.loc[(slice('Ada', 'Quinn'), 'Math'), ALL]
print(math_2)
#                   Exams     Labs
#                   I  II    I  II
# Stuent Course
# Ada    Math      71  73   75  74
# Quinn  Math      74  76   78  77

math_exams = df.loc[(ALL,'Math'),('Exams')]
print(math_exams)
#                I  II
# Stuent Course
# Ada    Math    71  73
# Quinn  Math    74  76
# Violet Math    77  79


math_II = df.loc[(ALL, 'Math'), (ALL, 'II')]
print(math_II)
#                 Exams Labs
#                  II   II
# Stuent Course
# Ada    Math      73   74
# Quinn  Math      76   77
# Violet Math      79   80



#Setting portions of a multi-index with xs
#http://stackoverflow.com/questions/19319432/pandas-selecting-a-lower-level-in-a-dataframe-to-do-a-ffill

