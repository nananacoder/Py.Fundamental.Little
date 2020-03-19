#!/usr/local/bin/python3.6
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

from sklearn.neural_network import MLPClassifier

path = 'diabetes.csv'
raw_data = pd.read_csv(path)
print(raw_data)
print(raw_data.describe())
nrow, ncol = raw_data.shape
print(nrow, ncol)
print("----correlation Matrix")
print(raw_data.corr())
pd.plotting.scatter_matrix(raw_data, figsize=[8,8])

predictors = raw_data.iloc[:,:ncol-1]
target = raw_data.iloc[:,-1]

pred_train, pred_test, tar_train, tar_test = train_test_split(predictors, target, test_size=0.3, random_state=1)

#  The default value is (100,) that is, 1 hidden layer with 100 neurons.
mlp = MLPClassifier(hidden_layer_sizes=(20,), max_iter=150)
mlp.fit(pred_train, np.ravel(tar_train, order='C'))
predictions = mlp.predict(pred_test)
print("Accuracy score of our model with MLP:", accuracy_score(tar_test, predictions))
# scores = cross_val_score(mlp, predictors, target, cv=10)
# print("Accuracy score of our model with MLP under cross validation:", scores.mean())

