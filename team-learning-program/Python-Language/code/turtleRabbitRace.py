#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019--2023, Luoo.
# All rights reserved.
'''
龟兔赛跑
'''
temp = input('请输入：')
inputArr = temp.split( )
v1 = int(inputArr[0])
v2 = int(inputArr[1])
t = int(inputArr[2])
s = int(inputArr[3])
l = int(inputArr[4])
# 比赛耗时
time = 0
win = ''
# 兔子进行跑步得耗时
j = 1
# 兔子还需等待得时间
wait = 0
# 根据乌龟耗时进行循环
for i in range(1, int(l/v2) + 1):
    # 耗时加1
    time += 1
    if v1*j == l:
        # 兔子抵达终点
        break
    elif v1*j - v2*i < t and wait == 0:
        # 兔子跑步时间加1
        j += 1
    elif wait != 0:
        # 兔子等待时间减1
        wait -= 1
    else:
        # 兔子等待时间重置
        wait = s
if time < int(l/v2):
    # 比赛耗时低于乌龟耗时，兔子获胜
    win = 'R'
elif v1*j == l:
    # 兔子实际跑步路程等于总赛程，平局
    win = 'D'
else:
    # 乌龟获胜
    win = 'T'
print(win)
print(time)