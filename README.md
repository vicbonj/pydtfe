[![DOI](https://zenodo.org/badge/76566234.svg)](https://zenodo.org/badge/latestdoi/76566234) [![Build Status](https://travis-ci.org/vicbonj/pydtfe.svg?branch=master)](https://travis-ci.org/vicbonj/pydtfe) [![Code Health](https://landscape.io/github/vicbonj/pydtfe/master/landscape.svg?style=flat)](https://landscape.io/github/vicbonj/pydtfe/master)

# density maps 2d and density cubes 3d

Author: Victor Bonjean

Mail: victor.bonjean@obspm.fr



A code to perform very easily and quickly density maps in 2d or in density cubes in 3d with a distribution of points in inputs, using the Delaunay Tesselation Field Estimator (PhD thesis: Schaap, W. E. (2007). DTFE: the Delaunay Tessellation Field Estimator s.n.), and scipy (http://www.scipy.org/).


- use "git clone https://github.com/vicbonj/pydtfe.git"
- in scripts/, run the notebooks with the command "jupyter-notebook Density_map_*d.ipynb" in 2 or 3d
- test the examples and create your own maps or cubes with your own distributions of points !

For 3d cube visualisation, you can use the "mayavi" library in python (http://docs.enthought.com/mayavi/mayavi/)

--- In terms of compatibility, it's better to have the environment Anaconda (https://anaconda.org) installed on your computer, either 2.7 or 3.6. Otherwise, there is a requirements.txt ---
