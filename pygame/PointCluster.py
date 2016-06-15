# -*- coding: utf-8 -*-

import numpy as np
import sklearn.cluster
import pygame, sys
from pygame.locals import *

'''
随机生成一些数据点并对它们进行聚类，也就是讲相近的点放在同一个聚类中
将计算一个关联矩阵(即包括关联值的矩阵， 如点与点之间的距离)
最后，使用scikit-learn中的AffinityPropagation类对数据点进行聚类
'''


# 在400*400的像素块中生成30个坐标点.
positions = np.random.randint(0, 400, size=(30, 2))

# 使用Euclidean distance 来初始化关联矩阵
positions_norms = np.sum(positions ** 2, axis=1)
S = - positions_norms[:, np.newaxis] - positions_norms[np.newaxis, :] \
    + 2 * np.dot(positions, positions.T)

# 将前面一步的结果提供给AffinityPropagation类。该类将为每一个数据点标记合适的聚类编号
# 创建AffinityPropagation对象并根据关联矩阵进行聚类
aff_pro = sklearn.cluster.AffinityPropagation().fit(S)
labels = aff_pro.labels_

# 为每一个聚类绘制多边形。需要的参数包括surface对象、颜色(红色)和数据点列表
polygon_points = []
for i in xrange(max(labels) + 1):
    polygon_points.append([])

#对数据点进行聚类
for i in xrange(len(labels)):
    polygon_points[labels[i]].append(positions[i])
pygame.init()
screen = pygame.display.set_mode((400, 400))

while True:
    for i in xrange(len(polygon_points)):
        pygame.draw.polygon(screen, (255, 0, 0), polygon_points[i])

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()




