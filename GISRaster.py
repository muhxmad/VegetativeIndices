#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
import os.path
from pathlib import Path
#%matplotlib inline


def NDVI_calculation(band4,band5):#NDVI function

    # ndvi calculation, empty cells or nodata cells are reported as 0
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')
    ndvi = np.where((nir + red) == 0., 0, (nir - red) / (nir + red))

    return ndvi

def RECI_calculation(band4,band5):#NDVI function

    # ndvi calculation, empty cells or nodata cells are reported as 0
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')
    ndvi = np.where((nir + red) == 0., 0, ((nir/red) - 1))

    return ndvi

def OSAVI_calculation(band4,band5):#OSAVI function

    # ndvi calculation, empty cells or nodata cells are reported as 0
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')
    ndvi = np.where((nir + red) == 0., 0, ((nir-red)/(nir+red+0.16)))

    return ndvi

def NDRE_calculation(band6, band5):#ndvi function
    # ndvi calculation, empty cells or nodata cells are reported as 0
    RE = band6.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    return np.where((nir + RE) == 0., 0, (nir - RE) / (nir + RE))

def GNDVI_calculation(band2, band5):  # GNDVI function
    # GNDVI calculation, empty cells or nodata cells are reported as 0
    gre = band2.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    gndvi = np.where((nir + gre) == 0., 0, (nir - gre) / (nir + gre))

    return gndvi

def NDWI_calculation(band2, band5):  # NDWI function
    # GNDVI calculation, empty cells or nodata cells are reported as 0
    gre = band2.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    gndvi = np.where((nir + gre) == 0., 0, (gre - nir) / (gre + nir))

    return gndvi

def LCI_calculation(band4, band5 ,band6):  # CLI function
    # CLI calculation, empty cells or nodata cells are reported as 0
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')
    re = band6.read(1).astype('float64')

    cli = np.where((nir + RE) == 0., 0, (nir - re) / (nir + red))

    return cli

def ARVI_calculation(band4, band5 ,band3):  # ARVI function
    # CLI calculation, empty cells or nodata cells are reported as 0
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')
    blue = band3.read(1).astype('float64')

    cli = np.where((nir + RE) == 0., 0, (((nir-(2*red)+blue)/(nir+(2*red)+blue))))

    return cli


filePathGre= 'C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Green.tif'
pathGRE= os.path.exists(filePathGre)
filePathred= 'C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Red.tif'
pathRed= os.path.exists(filePathred)
filePathBlu= 'C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_Blue.tif'
pathBlu= os.path.exists(filePathBlu)
filePathNIR= 'C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_NIR.tif'
pathNIR= os.path.exists(filePathNIR)
filePathRE= 'C:/Users/Asus/Desktop/Hua Xin/MULTI/map/result_RedEdge.tif'
pathRE= os.path.exists(filePathRE)

if (pathRed == True & pathNIR == True):#NDVI calculation
    # import bands as separate 1 band raster
    band4 = rasterio.open(filePathred)  # red
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    NDVI=NDVI_calculation(band4,band5)
    NDVI[:5, :5]

    ndviImage = rasterio.open('NDVI_py.tif', 'w', driver='Gtiff', width=band4.width, height=band4.height, count=1,
                              crs=band4.crs, transform=band4.transform, dtype='float64')
    ndviImage.write(NDVI, 1)
    ndviImage.close()

if (pathRed == True & pathNIR == True):#OSAVI calculation
    # import bands as separate 1 band raster
    band4 = rasterio.open(filePathred)  # red
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    OSAVI=OSAVI_calculation(band4,band5)
    OSAVI[:5, :5]

    OSAVIImage = rasterio.open('OSAVI_py.tif', 'w', driver='Gtiff', width=band4.width, height=band4.height, count=1,
                              crs=band4.crs, transform=band4.transform, dtype='float64')
    OSAVIImage.write(OSAVI, 1)
    OSAVIImage.close()

if (pathRE == True & pathNIR == True):  # NDRE calculation
    # import bands as separate 1 band raster
    band5 = rasterio.open(filePathNIR)  # nir
    band6 = rasterio.open(filePathRE)  # redEdge

    # generate nir and red objects as arrays in float64 format
    RE = band6.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    ndre = NDRE_calculation(band6, band5)
    ndre[:5, :5]

    ndreImage = rasterio.open('NDRE_py.tif', 'w', driver='Gtiff', width=band6.width, height=band6.height, count=1,
                              crs=band6.crs, transform=band6.transform, dtype='float64')
    ndreImage.write(ndre, 1)
    ndreImage.close()

if (pathGRE == True & pathNIR == True):  # GNDVI calculation
    # import bands as separate 1 band raster
    band2 = rasterio.open(filePathGre)  # nir
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    gre = band2.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    GNDVI = GNDVI_calculation(band2, band5)
    GNDVI[:5, :5]

    GNDVIImage = rasterio.open('GNDVI_py.tif', 'w', driver='Gtiff', width=band2.width, height=band2.height, count=1,
                              crs=band2.crs, transform=band2.transform, dtype='float64')
    GNDVIImage.write(GNDVI, 1)
    GNDVIImage.close()

if (pathGRE == True & pathNIR == True):  # NDWI calculation
    # import bands as separate 1 band raster
    band2 = rasterio.open(filePathGre)  # nir
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    gre = band2.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    NDWI = NDWI_calculation(band2, band5)
    NDWI[:5, :5]

    NDWIImage = rasterio.open('NDWI_py.tif', 'w', driver='Gtiff', width=band2.width, height=band2.height, count=1,
                              crs=band2.crs, transform=band2.transform, dtype='float64')
    NDWIImage.write(NDWI, 1)
    NDWIImage.close()

if (pathRed == True & pathNIR == True):#Red-Edge Chlorophyll Vegetation Index (RECl) calculation
    # import bands as separate 1 band raster
    band4 = rasterio.open(filePathred)  # red
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    red = band4.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    RECl=RECI_calculation(band4,band5)
    RECl[:5, :5]

    REClImage = rasterio.open('RECI_py.tif', 'w', driver='Gtiff', width=band4.width, height=band4.height, count=1,
                              crs=band4.crs, transform=band4.transform, dtype='float64')
    REClImage.write(RECl, 1)
    REClImage.close()

if (pathRed == True & pathNIR == True & pathRE == True):  # LCI calculation
    # import bands as separate 1 band raster
    band4 = rasterio.open(filePathred)  # red
    band6 = rasterio.open(filePathRE)  # redEdge
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    red = band4.read(1).astype('float64')
    RE = band6.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    LCI = LCI_calculation(band4, band5, band6)
    LCI[:5, :5]

    LCIImage = rasterio.open('LCI_py.tif', 'w', driver='Gtiff', width=band4.width, height=band4.height, count=1,
                              crs=band4.crs, transform=band4.transform, dtype='float64')
    LCIImage.write(LCI, 1)
    LCIImage.close()

if (pathRed == True & pathNIR == True & pathBlu == True):  # ARVI calculation
    # import bands as separate 1 band raster
    band4 = rasterio.open(filePathred)  # red
    band3 = rasterio.open(filePathBlu)  # blue
    band5 = rasterio.open(filePathNIR)  # nir

    # generate nir and red objects as arrays in float64 format
    red = band4.read(1).astype('float64')
    blue = band3.read(1).astype('float64')
    nir = band5.read(1).astype('float64')

    ARVI = ARVI_calculation(band4, band5, band3)
    ARVI[:5, :5]

    ARVIImage = rasterio.open('ARVI_py.tif', 'w', driver='Gtiff', width=band4.width, height=band4.height, count=1,
                              crs=band4.crs, transform=band4.transform, dtype='float64')
    ARVIImage.write(ARVI, 1)
    ARVIImage.close()