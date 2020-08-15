#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019--2023, luoo.
# All rights reserved.
'''
猜测0，100中的随机数字
'''
import random
correctNum = random.randrange(0,100)
guestNum = 101
count = 0
while correctNum != guestNum:
    count += 1
    temp = input("第" + str(count) + "次猜，请输入一个整形数字: ")
    try:
        guestNum = int(temp)
    except ValueError:
        print('输入无效')
        continue
    if guestNum == correctNum:
        print('恭喜你猜到了这个数是: ', correctNum)
        break
    elif guestNum < correctNum:
        print('太小')
        continue
    else:
        print('太大')
        continue