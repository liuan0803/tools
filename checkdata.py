# -*- coding:utf-8 -*-
import csv
import os
import glob
import sys
import shutil
import os
import cv2
import xml.etree.ElementTree as ET

"""
目的：将原图片(img)与其xml(xml)，合成为打标记的图片(labelled)，矩形框标记用红色即可
已有：（1）原图片文件夹(imgs_path)，（2）xml文件夹(xmls_path)
思路：
    step1: 读取（原图片文件夹中的）一张图片
    step2: 读取（xmls_path）该图片的xml文件，并获取其矩形框的两个对角顶点的位置
    step3: 依据矩形框顶点坐标，在该图片中画出该矩形框
    step4: 图片另存为'原文件名'+'_labelled'，存在‘lablled’文件夹中
"""

def xml_jpg2labelled(imgs_path, xmls_path, labelled_path):
    '''
    xml_jpg2labelled 把标签画在对应的原图上面，并保存到指定文件夹
    :param imgs_path: 原图路径
    :param xmls_path: 标签路径
    :param labelled_path: 输出文件夹路径
    :return:
    '''
    imgs_list = os.listdir(imgs_path)
    xmls_list = os.listdir(xmls_path)
    nums = len(imgs_list)
    for i in range(nums):
        img_path = os.path.join(imgs_path, imgs_list[i])
        xml_path = os.path.join(xmls_path, xmls_list[i])
        img = cv2.imread(img_path)
        labelled = img
        root = ET.parse(xml_path).getroot()
        objects = root.findall('object')
        for obj in objects:
            name = obj.find('name').text.strip()
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text.strip())
            ymin = int(bbox.find('ymin').text.strip())
            xmax = int(bbox.find('xmax').text.strip())
            ymax = int(bbox.find('ymax').text.strip())
            labelled = cv2.rectangle(labelled, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
            cv2.putText(labelled, name, (xmin, max(ymin - 2, 0)), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 255, 0), 1)
        cv2.imwrite('%slabelled_%s' % (labelled_path + '/', imgs_list[i]), labelled)
        # cv.imshow('labelled', labelled)
        # cv.imshow('origin', origin)
        # cv.waitKey()


if __name__ == '__main__':
    # imgs_path = r'F:\post_graduate_design\infared_plane_data\traindata_new\orgdata'
    # xmls_path = r'F:\post_graduate_design\infared_plane_data\traindata_new\orgxml'
    # labelled_path = r'F:\post_graduate_design\postgraduate_continue\check_data_and_sign\check_bbox_on_img\traindata'

    imgs_path = r'F:\post_graduate_design\infared_plane_data\traindata_new\output\jpgout'
    xmls_path = r'F:\post_graduate_design\infared_plane_data\traindata_new\output\xmlout'
    labelled_path = r'F:\post_graduate_design\postgraduate_continue\check_data_and_sign\check_bbox_on_img\testdata'
    xml_jpg2labelled(imgs_path, xmls_path, labelled_path)
