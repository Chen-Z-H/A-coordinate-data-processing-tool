# -*- coding=utf-8 -*-

import pandas as pd
import numpy as np
from shapely.geometry import Point
from shapely.geometry import Polygon

points_inside_file = "points_inside.csv"
points_outside_file = "points_outside.csv"

def _classify(datapath, coorpath, category, mode):
    inside_index_list = []  # coors of points inside the given area
    outside_index_list = []  # coors of points outside the given area
    coor = pd.read_csv(coorpath, engine='python')
    num_coor = coor['lat'].count()
    print(num_coor)
    coor_list = [None] * num_coor
    print("aaaa")
    # build the Polygon
    for i in range(num_coor):
        coor_list[i] = (coor.loc[i, 'lon'], coor.loc[i, 'lat'])
    # print(coor_list)
    area = Polygon(coor_list)

    data = pd.read_csv(datapath, engine='python')
    # print(data.dtypes)
    num_data_item = data['lat'].count()
    # print(num_data_item)
    for i in range(num_data_item):
        print("%f, %f" % (float(data.loc[i, 'lon']), float(data.loc[i, 'lat'])))
        if area.contains(Point(float(data.loc[i, 'lon']), float(data.loc[i, 'lat']))):
            inside_index_list.append(i)
        else:
            outside_index_list.append(i)
        # if i % 100 == 0:
        #     print("03")
        #     # self.saveProgressBar.setValue(int(i / num_data_item))
    print("dddd")

    # Save data to csv files
    points_inside_path = category + '\\' + points_inside_file
    points_outside_path = category + '\\' + points_outside_file
    if (mode == 0):
        data.iloc[inside_index_list].to_csv(points_inside_path, encoding='utf_8_sig')
    elif (mode == 1):
        data.iloc[outside_index_list].to_csv(points_outside_path, encoding='utf_8_sig')
    else:
        data.iloc[inside_index_list].to_csv(points_inside_path, encoding='utf_8_sig')
        data.iloc[outside_index_list].to_csv(points_outside_path, encoding='utf_8_sig')

# coor = pd.read_csv(r"E:\code\pycharm\DataProcessingTool\data\\渤海湾.csv", engine="python")

# coor_list = [None] * 10
# print(coor_list)
#
# area = Polygon([(121.54433333, 40.74293333), (121.04341667, 40.64138333), (120.70518333, 40.31398333), (120.45018333, 40.1143), (119.51341667, 39.69296667), (119.48928333, 39.40843333), (119.06935, 39.13795), (118.82141667, 38.9318), (118.57331667, 38.85328333), (118.31805, 38.95731667), (118.03231667, 39.03763333), (117.76201667, 38.86513333), (117.68955, 38.44665), (118.11353333, 38.28103333), (118.52921667, 38.25015), (118.97743333, 38.18971667), (119.22568333, 38.04615), (119.4189, 37.73338333), (119.1752, 37.54391667), (119.29826667, 37.39046667), (119.47636667, 37.3399), (119.70505, 37.29625), (119.9799, 37.53), (120.17501667, 37.7409), (120.6659, 37.89331667), (120.94511667, 37.94718333), (121.46558333, 37.79781667), (121.72275, 37.6153), (122.17546667, 37.55601667), (122.71606667, 37.3835), (122.94463333, 37.31381667), (124.7506, 37.58828333), (124.82146667, 37.99286667), (124.6369, 38.12305), (124.80388333, 38.41288333), (125.01043333, 39.02105), (125.21698333, 39.37015), (124.30826667, 39.68731667), (123.99843333, 39.71948333), (125.58555, 39.63176667), (123.04923333, 39.50441667), (122.17915, 39.07623333), (121.74901667, 38.76366667), (121.02605, 38.68826667), (121.04141667, 39.00298333), (121.50936667, 39.20576667), (121.07406667, 39.49936667), (121.65163333, 39.99828333), (122.06948333, 40.31831667), (122.0125, 40.58755), (121.80813333, 40.71758333), (121.51795, 40.77365)])
# print(area.contains(Point(120.735173, 34.18304)))

datapath = "E:\code\pycharm\DataProcessingTool\data\筛选.csv"
coorpath = "E:\code\pycharm\DataProcessingTool\data\coor.csv"
category = "E:\code\pycharm\DataProcessingTool\split"

_classify(datapath, coorpath, category, 2)





