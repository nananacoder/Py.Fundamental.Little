#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import itertools
import pandas as pd
import numpy as np


"""
Sort by specific column or an ordered list of columns, with a multi-index
http://stackoverflow.com/questions/14733871/mutli-index-sorting-in-pandas
"""

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

sv_df = df.sort_values(by=('Labs', 'II'), ascending=False)
print(sv_df)

#                    Exams     Labs
#                   I  II    I  II
# Stuent Course
# Violet Sci       78  81   81  81
#        Math      77  79   81  80
#        Comp      76  77   78  79
# Quinn  Sci       75  78   78  78
#        Math      74  76   78  77
#        Comp      73  74   75  76
# Ada    Sci       72  75   75  75
#        Math      71  73   75  74
#        Comp      70  71   72  73
