#!/usr/bin/env python2.7
# encoding=utf-8

from numpy import *
from os import listdir
import operator
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def createDataSet():
    """
    创建数据集 和 标签(分类)
    :return:
        group: 矩阵,每行包含不同的数据
        labels: 每个数据点的标签信息
        labels的元素个数 = group 矩阵行数
    """
    group = array([
        [1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def file2matrix(filename):
    """
    将待处理数据的格式改变为分类器可以接受的格式.
    :param filename: 样本数据文件
    :return: 训练样本矩阵和类标签
    """

    fr = open(filename)
    array_Lines = fr.readlines()
    fr.close()
    number_Lines = len(array_Lines)

    dataset = zeros((number_Lines, 3))
    data_Labels = []

    for index,line in enumerate(array_Lines):
        List_line = line.strip().split()

        dataset[index,:] = List_line[0:3]
        data_Labels.append(int(List_line[-1]))

    return dataset, data_Labels


def classify0(inX, dataSet, labels, k):
    """kNN分类器

    :param inX: 将要用于分类的输入向量
    :param dataSet: 训练样本集
    :param labels: 标签向量
    :param k: 用于选择最近邻居的数目

    labels标签向量的元素数目和矩阵dataSet的行数相同

    :return:
    """
    dataSetSize = dataSet.shape[0]

    # 欧式距离公式(计算两个向量点xA和xB之间的距离)
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
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
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1 #count

    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]




def showPic(dataset, datalabels):
    """绘制散点图

    """
    # datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
    # ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
    ax.scatter(dataset[:, 0],
               dataset[:, 1],
               dataset[:, 2],
               s=15.0 * array(datalabels),#大小
               c=15.0 * array(datalabels)) #颜色
    plt.show()


def autoNorm(dataSet):
    """ 数值归一化处理,使得输入的特征权重一致

    将任意取值范围的特征值转化为0到1区间内的值:
         newValue = (oldValue - min)/(max - min)
    :param dataSet: 特征值矩阵 1000*3矩阵
    :return: normDataSet: 归一化矩阵
             ranges: 取值范围
             minVals: 最小值矩阵
    """

    minVals = dataSet.min(0) # 每列最小值 1*3矩阵
    maxVals = dataSet.max(0) # 每列最大值 1*3矩阵
    ranges = maxVals - minVals # 取值范围 1*3矩阵

    # normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1)) # tile函数将变量内容复制成输入矩阵同样大小的矩阵.
    normDataSet = normDataSet/tile(ranges, (m,1)) # 特征值相除

    return normDataSet, ranges, minVals


def datingClassTest():
    """ 测试

    :return:
    """
    ratio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)

    # 测试向量的数量
    m = normMat.shape[0]
    num_Test = int(m*ratio)
    errorCount = 0.0

    for i in range(num_Test):
        classifierResult = classify0(normMat[i, :], normMat[num_Test:m, :], datingLabels[num_Test:m], 3)
        print "the classifier came back with: %d, the real answer is:%d" % (classifierResult, datingLabels[i])

        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" % (errorCount/float(num_Test))


def classifyPerson():
    resultList = ['完全不感兴趣', '可能喜欢', '很有可能喜欢']
    ffMiles = float(raw_input("每年搭乘飞机的飞行里程数?\n"))
    percentTats = float(raw_input("消耗在玩游戏上的时间百分比?\n:"))
    iceCream = float(raw_input("每周消费的冰淇淋公升数?\n"))

    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')

    normMat, ranges, minVals = autoNorm(datingDataMat)
    showPic(normMat, datingLabels)
    inArr = array([ffMiles, percentTats, iceCream])

    classifierResult = classify0((inArr-minVals)/ranges, normMat, datingLabels, 5)

    print "预测你对这个人: ",resultList[classifierResult-1]



def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []

    trainingFileList = listdir('trainingDigits')

    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0]) #从文件名解析分类数字

        hwLabels.append(classNumStr)

        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)

    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)

    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])

        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)

        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)

        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if classifierResult != classNumStr:
            errorCount += 1.0

    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is:%d" % (errorCount/float(mTest))


if __name__ == '__main__':

    # groups, labels = createDataSet()
    # print classify0([0.0], groups, labels, 3)
    # datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    # print autoNorm(datingDataMat)

    # datingClassTest()

    classifyPerson()
    # handwritingClassTest()