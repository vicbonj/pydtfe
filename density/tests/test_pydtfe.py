from pydtfe import map_dtfe2d, map_dtfe3d
import numpy as np
import numpy.testing as npt

def create_x_grid_2d(shape):
    x = []
    for i in range(shape):
        if i%2 == 1:
            x.append(np.arange(shape))
        else: x.append(np.arange(shape)+0.5)
    return np.array(x).ravel()

def create_y_grid_2d(shape):
    y = []
    for i in range(shape):
        y.append(np.ones(shape)*i)
    return np.array(y).ravel()

def create_hexa_2d(shape):
    x = create_x_grid_2d(shape)
    y = create_y_grid_2d(shape)
    return x, y

def test_map_dtfe2d():
    size = 100
    x, y = create_hexa_2d(size)
    grid = map_dtfe2d(x, y, size)
    npt.assert_array_equal(grid[1:-1,2:-2], np.ones((size, size))[1:-1,2:-2])

def create_hexalike_3d(shape):
    s = np.arange(shape)
    x, y, z, = np.meshgrid(s, s, s)
    x*=2; y*=2; z*=2
    xx, yy, zz = np.meshgrid(s, s, s)
    xx=(xx+0.5)*2; yy=(yy+0.5)*2; zz=(zz+0.5)*2
    x = np.hstack([x, xx])
    y = np.hstack([y, yy])
    z = np.hstack([z, zz])
    return x.ravel(), y.ravel(), z.ravel()

def test_map_dtfe3d():
    size = 10
    x, y, z = create_hexalike_3d(size)
    grid = map_dtfe3d(x, y, z, size)
    npt.assert_array_equal(grid[2:-2,2:-2,2:-2], np.ones((size, size, size))[2:-2,2:-2,2:-2]*0.25)
