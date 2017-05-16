import numpy as np
from scipy.spatial import Delaunay
from itertools import repeat
from multiprocessing import Pool
from scipy.interpolate import griddata
from astropy.cosmology import Planck15

def how_many(tri,num_points):
    there_are=np.where(tri.simplices==num_points)[0]
    return there_are

def area_triangle(points):
    return 0.5*np.abs(np.dot(points[:,0],np.roll(points[:,1],1))-np.dot(points[:,1],np.roll(points[:,0],1)))

def area_delaunay(inputs):
    tri,num=inputs
    a=area_triangle(tri.points[tri.simplices[num]])
    return a

def get_areas(tri,the_pool):
    shape=tri.simplices.shape[0]
    areas=np.empty(shape)
    all_inputs=zip(repeat(tri),np.arange(shape))
    areas=the_pool.map(area_delaunay,all_inputs)
    return np.array(areas)

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

def get_densities3d(inputs):
    tri,num,volumes=inputs
    l=how_many(tri,num)
    true_vol=np.sum(volumes[l])/4.
    return 1./true_vol

def densities3d(tri,the_pool,volumes):
    shape=tri.points.shape[0]
    dens=np.empty(shape)
    all_inputs=zip(repeat(tri),np.arange(shape),repeat(volumes))
    dens=the_pool.map(get_densities3d,all_inputs)
    return np.array(dens)

def get_densities2d(inputs):
    tri,num,areas=inputs
    l=how_many(tri,num)
    true_vol=np.sum(areas[l])/3.
    return 1./true_vol

def densities2d(tri,the_pool,areas):
    shape=tri.points.shape[0]
    dens=np.empty(shape)
    all_inputs=zip(repeat(tri),np.arange(shape),repeat(areas))
    dens=the_pool.map(get_densities2d,all_inputs)
    return np.array(dens)

def map_dtfe3d(x,y,z,size):
    tab=np.vstack((x,y,z)).T
    tri=Delaunay(tab)
    the_pool=Pool()
    volumes=get_volumes(tri,the_pool)
    d=densities3d(tri,the_pool,volumes)
    the_pool.close()
    x_m=np.linspace(np.min(x),np.max(x),size)
    y_m=np.linspace(np.min(y),np.max(y),size)
    z_m=np.linspace(np.min(z),np.max(z),size)
    x_m,y_m,z_m=np.meshgrid(x_m,y_m,z_m)
    grid=griddata(tab,d,(x_m,y_m,z_m),method='linear')
    grid[np.isnan(grid)]=0
    return grid

def map_dtfe2d(x,y,size):
    tab=np.vstack((x,y)).T
    tri=Delaunay(tab)
    the_pool=Pool()
    areas=get_areas(tri,the_pool)
    d=densities2d(tri,the_pool,areas)
    the_pool.close()
    x_m=np.linspace(np.min(x),np.max(x),size)
    y_m=np.linspace(np.min(y),np.max(y),size)
    x_m,y_m=np.meshgrid(x_m,y_m)
    grid=griddata(tab,d,(x_m,y_m),method='linear')
    grid[np.isnan(grid)]=0
    return grid
