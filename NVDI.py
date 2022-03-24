from osgeo import gdal
import cv2
import numpy as np
import skimage.exposure as exposure
from numpy import *
import os

#simple normalization between range of 0 to 1
def NormalizeData(data):
    #return (data - np.min(data)) / (np.max(data) - np.min(data))
    for i, pix in enumerate(data):
        filename = f"array_1_frame-{i}.tif"
        #print(f"Processing frame {i} into file {filename}")
        # normalize image to 8-bit range
        img_norm = exposure.rescale_intensity(pix, in_range='image', out_range=(0, 255)).astype(np.uint8)

    return img_norm

g = gdal.Open('C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Red.tif', 1)
redB = g.ReadAsArray()
g = gdal.Open("C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_NIR.tif",1)
nirB = g.ReadAsArray()

red=NormalizeData(redB)
nir=NormalizeData(nirB)
#red = array(red, dtype = float)
#nir = array(nir, dtype = float)
red = np.array(red, dtype = float)
nir = np.array(nir, dtype = float)
check = np.logical_and (red > 0, nir > 0)
ndvi = np.where ( check,  (nir - red ) / ( nir + red ),(nir + red ) / ( nir - red ) )
geo = g.GetGeoTransform()
proj = g.GetProjection()
shape = red.shape
driver = gdal.GetDriverByName("GTiff")
dst_ds = driver.Create( "ndviNorm_py.tif", shape[1], shape[0], 1, gdal.GDT_Float32)
dst_ds.SetGeoTransform( geo )
dst_ds.SetProjection( proj )
dst_ds.GetRasterBand(1).WriteArray(ndvi)
dst_ds = None  # save, close