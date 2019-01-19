# Import GDAL, NumPy, and matplotlib
from osgeo import gdal, gdal_array
import numpy as np
import scipy

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

#IMAGE
b1_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/clip_b1r.tif', gdal.GA_ReadOnly)
b1_09 = b1_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b1_09 = b1_09.ravel()

b2_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/clip_b2r.tif', gdal.GA_ReadOnly)
b2_09 = b2_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b2_09 = b2_09.ravel()

b3_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/clip_b3r.tif', gdal.GA_ReadOnly)
b3_09 = b3_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b3_09 = b3_09.ravel()

b4_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/clip_b4r.tif', gdal.GA_ReadOnly)
b4_09 = b4_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b4_09 = b4_09.ravel()

b5_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/clip_b5r.tif', gdal.GA_ReadOnly)
b5_09 = b5_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b5_09 = b5_09.ravel()

b7_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/clip_b7r.tif', gdal.GA_ReadOnly)
b7_09 = b7_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b7_09 = b7_09.ravel()

ndvi_09_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2009/ndvi.tif', gdal.GA_ReadOnly)
ndvi_09 = ndvi_09_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
ndvi_09 = ndvi_09.ravel()

#stack these bands
img_09 = np.array([b1_09,b2_09,b3_09,b4_09,b5_09,b7_09,ndvi_09])
img_09 = img_09.transpose()

#saving the resulting array into .npy
np.save("/Volumes/ga87rif/Study Project/satelite images/Level-2/img_09.npy", img_09)