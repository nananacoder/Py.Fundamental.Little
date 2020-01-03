#!/usr/bin/python2.7
# -*-coding:utf-8-*-

"""iris: 鸢尾植物，这里存储了其萼片和花瓣的长宽，一共4个属性
鸢尾植物又分三类: 'setosa' 'versicolor' 'virginica'
"""

import operator
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def iris_data():
    iris = load_iris()
    species = iris['target_names'] # 'setosa' 'versicolor' 'virginica'
    data = iris['data']
    features = iris['feature_names']
    target = iris['target']

    # traing_data, test_data, traing_labels, test_labels = train_test_split(data, target, random_state=0)
    return data,target

def knn_classifier(X, dataSet, data_labels,k):
    
    dataSet_Size = dataSet.shape[0]
    # 欧式距离公式(计算两个向量点xA和xB之间的距离)
    diffMat = np.tile(X, (dataSet_Size, 1)) - dataSet
    distances = ((diffMat**2).sum(axis=1))**0.5

    # 计算完所有点之间的距离后, 可以对数据按照从小到大的次序排序.
    # 选择距离最小的k个点,确定这些点的主要分类
    # 将classCount字典分解为元组列表,
    # 然后使用operator.itemgetter方法,按照第二个元素的次序对元组进行排序
    # 此处的排序为逆序, 即按照从大到小次序排序
    # 最后返回发生频率最高的元素标签.
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = data_labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 #count

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]

def classifier_Test():
    """ 测试算法
    """
    data,target = iris_data()
    traing_data, test_data, traing_labels, test_labels = train_test_split(data, target, random_state=0)

    # ratio = 0.10
    # datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    # normMat, ranges, minVals = autoNorm(datingDataMat)
    #
    # # 计算测试向量的数量
    # m = normMat.shape[0]
    # num_Test = int(m*ratio)
    errorCount = 0.0
    num_Test = test_data.shape[0]

    for i in range(num_Test):
        classifierResult = knn_classifier(test_data[i,:], traing_data, traing_labels, 3)
        # print "the classifier came back with: %d, the real answer is:%d" % (classifierResult, test_labels[i])

        if (classifierResult != test_labels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(num_Test))

def picture():
    tra_data, tra_labels =iris_data()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(tra_data[:,0],
               tra_data[:,1],
               tra_data[:,2],
               s=15.0 * np.array(tra_labels+1),
               c=20.0 * np.array(tra_labels+1))
    plt.show()

def predict():
    X_new = np.array([[5, 2.9, 1, 1.2]])
    dataset,data_labels = iris_data()
    knn_result = knn_classifier(X_new,dataset,data_labels,4)
    species = {0:'setosa', 1:'versicolor', 2:'virginica'}
    print species[knn_result]

if __name__ == '__main__':
    # classifier_Test()
    # picture()
    predict()