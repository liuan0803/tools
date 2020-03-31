# -*- encoding: utf-8 -*-
'''
@File    :   move_file_name.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/3/4 16:20
@Desciption  :   None
'''

import numpy as np
import shutil
import os

#读取txt文件
train_txt = open('D:/liuan58/ocrdata/xingming-opt/liuyan_data/txtsave/train.txt')
train_content = train_txt.readlines()   #保存的train.txt中的内容

file_path = r'D:\liuan58\ocrdata\xingming-opt\drivinglic_1_trainval\Annotations_1'
jpg_dir_list = os.listdir(file_path)

print("train_content:", train_content)

for each_xml_dir in jpg_dir_list:
    a = each_xml_dir.split('.')[-2] + '\n'
    print("a", a)
    if  a in train_content:
        shutil.move(file_path + '/' + each_xml_dir, r'D:\liuan58\ocrdata\xingming-opt\liuyan_data\xingming_xml_2000_liuyan')

print("successed!")