#-*- coding: UTF-8 -*-

import numpy as np

from copy import deepcopy
import csv
import os
import glob
import sys
import pandas as pd


#############输入的类别名称###########
classes = ["PlateNo","Model","VIN","lx","xm","zz","xz","no","zc","fz"]
###########原始txt文件绝对路径########
pathtxt = "/data/liuan/project/retina_attention/retinanet/2007_train.txt"
###########xml保存的目标路径##########
###########这样保存的是指定路径，名称也是很长，自己改一下就行############
pathsavexml = "\\data\\liuan\\project\\retina_attention\\retinanet"


def txt_to_csv():
    xml_list = []
    with open(pathtxt) as f:
        lines = f.readlines()
        for nums ,line in enumerate(lines):
            chars = line.strip().split(' ')
            samehead = chars[0] ####图片路径名称
            for i in range(1, len(chars)):
                if(len(chars) < 10):
                    print("nums",nums,"len_label",len(chars))
                curr = chars[i]
                curr = curr.strip().split(',')
                category = classes[int(curr[-1])]####类别####
                x1 = int(curr[-5])
                y1 = int(curr[-4])
                x2 = int(curr[-3])
                y2 = int(curr[-2])

                value = (samehead, x1,y1,x2,y2,category)
                xml_list.append(value)


    column_name = ['jpgpath','x1','y1','x2','y2','category']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df

def main():
    xml_df = txt_to_csv()
    xml_df.to_csv(pathsavexml + '_train.csv', index=None)
    print('Successfully converted txt to csv.')

main()