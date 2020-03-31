# -*- encoding: utf-8 -*-
'''
@File    :   move_file_by_name.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/2/25 15:56
@Desciption  :   None
'''

import numpy as np
import shutil
import os

file_path = 'D:/liuan58/keras-retinanet-master/bbox_xml/labelimg_data'
jpg_dir_list = os.listdir(file_path)
need_classes = ['zc', 'fz']

for each_xml_dir in jpg_dir_list:
    classes = (each_xml_dir.split('.')[0]).split('_')[-1]
    print("classes:", classes)
    if classes not in need_classes:
        shutil.move(file_path + '/' + each_xml_dir, 'D:/liuan58/keras-retinanet-master/bbox_xml' + '/' + 'a')
