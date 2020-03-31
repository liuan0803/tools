#! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image

# VEDAI 图像存储位置
src_img_dir = "F:/traindata2/jpgchuli/orgdata"
# VEDAI 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = "F:/traindata2/save"
src_xml_dir = "F:/traindata2/orgxml"

img_Lists = glob.glob(src_img_dir + '/*.jpg')

img_basenames = []  # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))

img_names = []  # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)

for img in img_names:
    im = Image.open((src_img_dir + '/' + img + '.jpg'))
    width, height = im.size

    # open the crospronding txt file
    gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
    # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
    # xml_file.write('    <filename>' + str(img) + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')

    # write the region of image on xml file
    for img_each_label in gt:
        spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
        xml_file.write('    <object>\n')
        xml_file.write('        <name>' + str(spt[4]) + '</name>\n')
        xml_file.write('        <pose>Unspecified</pose>\n')
        xml_file.write('        <truncated>0</truncated>\n')
        xml_file.write('        <difficult>0</difficult>\n')
        xml_file.write('        <bndbox>\n')
        xml_file.write('            <xmin>' + str(int(float(spt[0]))) + '</xmin>\n') #这个后面加了强制转换的，要先转为float再转int，否则会报错
        xml_file.write('            <ymin>' + str(int(float(spt[1]))) + '</ymin>\n')
        xml_file.write('            <xmax>' + str(int(float(spt[2]))) + '</xmax>\n')
        xml_file.write('            <ymax>' + str(int(float(spt[3]))) + '</ymax>\n')
        xml_file.write('        </bndbox>\n')
        xml_file.write('    </object>\n')

    xml_file.write('</annotation>')