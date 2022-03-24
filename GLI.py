from osgeo import gdal
import numpy as np
from numpy import *
import os

g = gdal.Open('C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Red.tif', 1)
re = g.ReadAsArray()
g = gdal.Open('C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Blue.tif', 1)
blu = g.ReadAsArray()
g = gdal.Open('C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Green.tif', 1)
gre = g.ReadAsArray()
g = gdal.Open("C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_NIR.tif",1)
nir = g.ReadAsArray()

RE = array(re, dtype = float)
BLU = array(blu, dtype = float)
GRE = array(gre, dtype = float)
nir = array(nir, dtype = float)
check = np.logical_and (GRE>0, nir > 0)
GLI = np.where ( check, ((2*GRE)-RE-BLU)/((2*GRE)+RE+BLU),((2*GRE)+RE+BLU) /((2*GRE)-RE-BLU) )
geo = g.GetGeoTransform()
proj = g.GetProjection()
shape = GRE.shape
driver = gdal.GetDriverByName("GTiff")
dst_ds = driver.Create( "GLI_py.tif", shape[1], shape[0], 1, gdal.GDT_Float32)
dst_ds.SetGeoTransform( geo )
dst_ds.SetProjection( proj )
dst_ds.GetRasterBand(1).WriteArray(GLI)
dst_ds = None  # save, close