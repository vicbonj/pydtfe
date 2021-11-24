#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.spatial import Delaunay
from multiprocessing import Pool
from scipy.interpolate import griddata
import time
import matplotlib.pyplot as plt
from tqdm import tqdm

__all__ = ["Pydtfe"]


class Pydtfe:

    def __init__(self, x, y, xmin=None, xmax=None, ymin=None, ymax=None, xsize=500, ysize=500, weights=None):
        t0 = time.time()
        self.x = x
        self.y = y
        if xmin is None:
            self.xmin = self.x.min()
        else:
            self.xmin = xmin
        if xmax is None:
            self.xmax = self.x.max()
        else:
            self.xmax = xmax
        if ymin is None:
            self.ymin = self.y.min()
        else:
            self.ymin = ymin
        if ymax is None:
            self.ymax = self.y.max()
        else:
            self.ymax = ymax
        self.xsize = xsize
        self.ysize = ysize
        self.weights = weights
        self.tab = np.vstack((self.x, self.y)).T
        self.tri = Delaunay(self.tab)
        t1 = time.time()
        print('init:', t1 - t0)
        self.comp_areas()
        t2 = time.time()
        print('areas:', t2 - t1)
        self.comp_densities()
        t3 = time.time()
        print('densities:', t3 - t2)
        self.make_grid()
        t4 = time.time()
        print('make grid:', t4 - t3)
        print('total:', time.time() - t0)
    
    def area_triangle(self, points):
        return 0.5 * abs(np.linalg.det(points))

    def comp_areas(self):
        self.areas = self.area_triangle(np.concatenate([self.tri.points[self.tri.simplices], np.ones((len(self.tri.simplices), 3, 1))], axis=2))

    def comp_densities(self):
        self.sum_areas = np.zeros(len(self.tri.points))
        ravel = self.tri.vertices.ravel()
        for i in range(len(ravel)):
            self.sum_areas[ravel[i]] += self.areas[int(i/3)]
        self.densities = 3 / self.sum_areas

    def make_grid(self):
        x_m = np.linspace(self.xmin, self.xmax, self.xsize)
        y_m = np.linspace(self.ymin, self.ymax, self.ysize)
        self.x_m, self.y_m = np.meshgrid(x_m, y_m)
        self.data2grid = self.densities
        if self.weights is not None:
            self.data2grid *= self.weights
        self.grid = griddata(self.tab, self.data2grid, (self.x_m, self.y_m), method='linear')

    def show(self, log_scale=True, show_points=True):
        plt.figure()
        if log_scale:
            plt.imshow(np.log10(self.grid), origin='lower', extent=[self.xmin, self.xmax, self.ymin, self.ymax])
            leg = r'log($\rho$)'
        else:
            plt.imshow(self.grid, origin='lower', extent=[self.xmin, self.xmax, self.ymin, self.ymax])
            leg = r'$\rho$'
        if show_points:
            plt.plot(self.x, self.y, '+r')
        plt.xlabel('x', fontsize=15)
        plt.ylabel('y', fontsize=15)
        bar = plt.colorbar()
        bar.set_label(leg)
        plt.show()
