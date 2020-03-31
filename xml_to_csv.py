# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 00:52:02 2018
@author: Xiang Guo
"""

import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# os.chdir('/data/liuyan/drivinglic/imagedata/drivinglic_1_trainval/Annotations')
xmls_path = 'E:\\data\\house\\1008\\marked\\detect\\2-batch\\2\\xmls_aug'
images_path = 'E:\\data\\house\\1008\\marked\\detect\\2-batch\\2\\images_aug'

def xml_to_csv():
    count = 0
    xml_list = []
    xml_file_list = os.listdir(xmls_path)
    # print(xml_file_list)
    # for xml_file in glob.glob(xmls_path + '/*.xml'):
    name_base = 10
    for xml_filename in xml_file_list:
        xml_file = os.path.join(xmls_path, xml_filename)
        image_filename = os.path.splitext(xml_filename)[0]+'.jpg'
        image_path = os.path.join(images_path, image_filename)
        print(image_path)
        if not os.path.exists(image_path):
            count += 1
            continue
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            name = int(member[0].text)
            name += name_base
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     str(name),
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            print(value)
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    print(count)
    return xml_df

def main():
    xml_df = xml_to_csv()
    xml_df.to_csv(xmls_path+'_train.csv', index=None)
    print('Successfully converted xml to csv.')

main()