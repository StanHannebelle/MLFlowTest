import numpy as np
import iris
import iris_grib
cubes = iris_grib.load_cubes('grib.grb2')
cubes=list(cubes)
print(np.shape(cubes[0].data))