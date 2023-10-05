# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def getblocks(self):

    # Replace with the actual file path
    file_path = '/home/ankitmittal/Documents/STUDY/RBE595/HW2a/amittal_p2a/src/sample_maps/map2.txt' 
    block_data= []
    block = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts or parts[0].startswith('#'):
                continue
            if parts[0] == 'boundary':
                boundary_data = [float(x) for x in parts[1:]]
                xmin, ymin, zmin, xmax, ymax, zmax= boundary_data
                self.boundary = np.array([xmin, ymin, zmin, xmax, ymax, zmax])
            elif parts[0] == 'block':
                block_data.append([float(x) for x in parts[1:]])
                xmin, ymin, zmin, xmax, ymax, zmax, r, g, b = block_data[-1]
                block.append([xmin,ymin,zmin,xmax,ymax,zmax])

    Obstacles = []
    for i in block:
        i = np.array(i)
        Obstacles.append([j for j in i])
    return np.array(Obstacles)

def getobstacle(blocks):
    # used in lineAABB
    AABB = []
    for i in blocks:
        bloated_bocks = np.reshape(np.array([np.add(i[0:3], -0.25), np.add(i[3:6],  0.25)]),6)
        AABB.append(aabb(bloated_bocks))
    return AABB


class aabb(object):
    # make AABB out of blocks, 
    def __init__(self,AABB):
        self.P = [(AABB[3] + AABB[0])/2, (AABB[4] + AABB[1])/2, (AABB[5] + AABB[2])/2]# center point
        self.E = [(AABB[3] - AABB[0])/2, (AABB[4] - AABB[1])/2, (AABB[5] - AABB[2])/2]# extents


class env():
    def __init__(self, xmin=0, ymin=-5, zmin=0, xmax=10, ymax=10, zmax=6, resolution=1):
        self.boundary = np.array([xmin, ymin, zmin, xmax, ymax, zmax]) 
        self.blocks = getblocks(self)
        self.AABB = getobstacle(self.blocks)
        self.start = np.array([0, 20, 2])
        self.goal = np.array([10, 20, 3])
        # self.start = np.array([0, 3, 2])
        # self.goal = np.array([20, 2, 4])
        self.t = 0 # time 

          
if __name__ == '__main__':
    newenv = env()
