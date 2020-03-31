#-*- coding: UTF-8 -*-

import numpy as np
import cv2 as cv
from copy import deepcopy

categories = 'trees2'
begin = 2010

with open("F:/traindata2/groundtruth.txt") as f:
    lines = f.readlines()

    for n ,line in enumerate(lines):
        tmps = []
        chars = line.strip().split(',')
        print(chars)
        # data = chars.deepcopy()
        #data = int(chars)
        # count = len(data)
        # targetnum = count / 2
        # for num in range(0,count,2):

        tmp = []
        # print(num)
        # x = data[num]
        # y = data[num + 1]
        x1 = chars[2]
        x2 = chars[3]
        y1 = chars[6]
        y2 = chars[7]
        tmp.append(x1)
        tmp.append(x2)
        tmp.append(y1)
        tmp.append(y2)
        tmp.append(categories)
        tmps.append(tmp)
        np.savetxt( "save/" + str(n + begin).zfill(7) + '.txt',np.array(tmps),fmt='%s')
        # print(data)