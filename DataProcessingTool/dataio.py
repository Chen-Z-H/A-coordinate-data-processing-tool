import numpy as np
import pandas as pd
from shapely.geometry import Point
from shapely.geometry import Polygon


points_inside_path = "points_inside.csv"
points_outside_path = "points_outside.csv"


def loadDataFile(path):
    data = pd.read_csv(path)
    return None

def loadCoorFile(path):
    coor = pd.read_csv(path)
    return None

def saveCsvFile(fullpath):
    return None

def contain():
    return None

def classify(datapath, coorpath, category, mode):
    inside_index_list = []          # coors of points inside the given area
    outside_index_list = []         # coors of points outside the given area

    coor = pd.read_csv(coorpath)
    num_coor = coor.count()
    coor_list = None * num_coor

    # build the Polygon
    for i in range(num_coor):
        coor_list[i] = (coor.loc[i, ['lon']], coor.loc[i, ['lat']])
    area = Polygon(coor_list)

    data = pd.read_csv(datapath)
    num_data_item = data.count()

    for i in range(num_data_item):
        if (area.contains(Point(data.loc[i, ['lon']], data.loc[i, ['lat']]))):
            inside_index_list.append(i)
        else:
            outside_index_list.append(i)

    if (mode == 0):
        pass
    elif (mode == 1):
        pass
    else:
        pass



