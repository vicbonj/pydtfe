import numpy as np
from scipy.spatial import Delaunay
from itertools import repeat
from multiprocessing import Pool
from scipy.interpolate import griddata
from astropy.cosmology import Planck15

def transform_shape(ra,dec,z):
    tab=np.zeros((ra.shape[0],3))
    tab[:,0]=ra
    tab[:,1]=dec
    tab[:,2]=z
    return tab

def how_many(tri,num_points):
    there_are=np.where(tri.simplices==num_points)[0]
    return there_are

def vol_tetrahedron(points):
    return abs(np.dot((points[0]-points[3]),np.cross((points[1]-points[3]),(points[2]-points[3]))))/6.

def vol_delaunay(inputs):
     tri,num=inputs
     a=vol_tetrahedron(tri.points[tri.simplices[num]])
     return a

def get_volumes(tri,the_pool):
    shape=tri.simplices.shape[0]
    volumes=np.empty(shape)
    all_inputs=zip(repeat(tri),np.arange(shape))
    volumes=the_pool.map(vol_delaunay,all_inputs)
    return np.array(volumes)

def get_densities(inputs):
    tri,num,volumes=inputs
    l=how_many(tri,num)
    true_vol=np.sum(volumes[l])/4.
    return 1./true_vol

def densities(tri,the_pool):
    shape=tri.points.shape[0]
    dens=np.zeros(shape)
    volumes=get_volumes(tri,the_pool)
    all_inputs=zip(repeat(tri),np.arange(shape),repeat(volumes))
    dens=the_pool.map(get_densities,all_inputs)
    return np.array(dens)

def map_dtfe(x,y,z,size):
    tab=transform_shape(x,y,z)
    tri=Delaunay(tab)
    the_pool=Pool()
    d=densities(tri,the_pool)
    the_pool.close()
    x_m=np.linspace(np.min(x),np.max(x),size)
    y_m=np.linspace(np.min(y),np.max(y),size)
    z_m=np.linspace(np.min(z1),np.max(z1),size)
    x_m,y_m,z_m=np.meshgrid(x_m,y_m,z_m)
    grid=griddata(tab,d,(x_m,y_m,z_m),method='linear')
    grid[np.isnan(grid)]=0
    return grid
