# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
import math

pygame.init()

clock = pygame.time.Clock()
# 创建一个游戏中的时钟对象
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Animating Objects')
img = pygame.image.load('logo.png')
# 萌萌的小狗转圈的轨迹
pos = []

# 萌萌的小狗转圈的半径
r = (400 - max(img.get_width(), img.get_height())) / 2

# 顺时针转上半圈
for x in range(-r, r + 1):
    y = math.sqrt(r * r - x * x)
    # 此时(x,y)在(0,0)为原点，r为半径的圆上，转成轨迹要加上r偏移～
    pos.append([x + r, y + r]);

# 顺时针转下半圈
for x in range(r, -(r + 1), -1):
    y = -math.sqrt(r * r - x * x)
    # 此时(x,y)在(0,0)为原点，r为半径的圆上，转成轨迹要加上r偏移～
    pos.append([x + r, y + r]);

i = 0

while True:
    #清屏
    screen.fill((255, 255, 255))

    screen.blit(img, pos[i % len(pos)])
    i += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)  #设置时钟周期。这里的30即每秒钟的帧数



