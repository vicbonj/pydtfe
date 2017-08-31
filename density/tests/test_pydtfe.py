from pydtfe import map_dtfe2d, map_dtfe3d
import numpy as np
import numpy.testing as npt

def create_x_grid(shape):
    x = []
    for i in range(shape):
        if i%2 == 1:
            x.append(np.arange(shape))
        else: x.append(np.arange(shape)+0.5)
    return np.array(x).ravel()

def create_y_grid(shape):
    y = []
    for i in range(shape):
        y.append(np.ones(shape)*i)
    return np.array(y).ravel()

def create_hexa(shape):
    x = create_x_grid(shape)
    y = create_y_grid(shape)
    return x, y

def test_map_dtfe2d():
    size = 100
    x, y = create_hexa(size)
    grid = map_dtfe2d(x, y, size)
    npt.assert_array_equal(grid[1:-1,2:-2], np.ones((size, size))[1:-1,2:-2])

