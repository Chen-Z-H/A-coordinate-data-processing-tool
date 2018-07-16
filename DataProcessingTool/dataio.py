import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry import Polygon


points_inside_file = "points_inside.csv"
points_outside_file = "points_outside.csv"


def loadDataFile(path):
    data = pd.read_csv(path)
    return None

def loadCoorFile(path):
    coor = pd.read_csv(path)
    return None

def saveCsvFile(fullpath):
    return None


def classify(datapath, coorpath, category, mode):
    inside_index_list = []          # coors of points inside the given area
    outside_index_list = []         # coors of points outside the given area
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
    print("bbbb")
    data = pd.read_csv(datapath, engine='python')
    num_data_item = data['lat'].count()
    print("cccc")
    for i in range(num_data_item):
        if (area.contains(Point(data.loc[i, 'lon'], data.loc[i, 'lat']))):
            inside_index_list.append(i)
        else:
            outside_index_list.append(i)
        if (i % 100 == 0):
            print(i)
    print("dddd")
    points_inside_path = category + '\\' + points_inside_file
    points_outside_path = category + '\\' + points_outside_file
    if (mode == 0):
        data.iloc[inside_index_list].to_csv(points_inside_path)
    elif (mode == 1):
        data.iloc[outside_index_list].to_csv(points_outside_path)
    else:
        data.iloc[inside_index_list].to_csv(points_inside_path)
        data.iloc[outside_index_list].to_csv(points_outside_path)



