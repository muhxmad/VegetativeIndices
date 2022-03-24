#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
#import bands as separate 1 band raster
band4 = rasterio.open('C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Red.tif') #red
band5 = rasterio.open('C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_NIR.tif') #nir
#number of raster rows
band4.height
band5.height
#number of raster columns
band4.width
band5.width
#type of raster byte
band4.dtypes[0]
band5.dtypes[0]
#raster sytem of reference
band4.crs
band5.crs
#raster transform parameters
band4.transform
band5.transform
#raster values as matrix array
band4.read(1)
band5.read(1)

#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

#nir
#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where((nir+red)==0.,0,(nir-red)/(nir+red))
ndvi[:5,:5]
#export ndvi image
ndviImage = rasterio.open('NDVI_py.tif','w',driver='Gtiff',width=band4.width,height = band4.height,count=1, crs=band4.crs,transform=band4.transform,dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()

