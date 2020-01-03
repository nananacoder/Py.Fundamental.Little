#!/usr/bin/python2.7
# -*-coding:utf-8-*-

"""iris: 鸢尾植物，这里存储了其萼片和花瓣的长宽，一共4个属性
鸢尾植物又分三类: 'setosa' 'versicolor' 'virginica'
"""


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()
species = iris['target_names']
data = iris['data']
features = iris['feature_names']
target = iris['target']

traing_data, test_data, traing_labels, test_labels = train_test_split(data, target, random_state=0)

labels = {0:"setosa",1:"versicolor",2:"virginica"}
def showPic():
    # 绘制散点图

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(traing_data[:, 0],
               traing_data[:, 1],
               traing_data[:, 2],
               s=15.0 * np.array(traing_labels+1),#大小
               c=20.0 * np.array(traing_labels+1)) #颜色
    plt.show()

knn = KNeighborsClassifier(n_neighbors=1, weights='distance')
knn.fit(traing_data, traing_labels)

def prediction():
    test_sc = knn.score(test_data, test_labels)
    print test_sc
    X_new = np.array([[5, 2.9, 1, 0.2]])
    pre_num = knn.predict(X_new)
    print labels[pre_num[0]]


if __name__ == '__main__':
    prediction()