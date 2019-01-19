# Import GDAL, NumPy, and matplotlib
from osgeo import gdal, gdal_array
import numpy as np
import scipy

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

#IMAGE
b1_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/clip_b1r.tif', gdal.GA_ReadOnly)
b1_11 = b1_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b1_11 = b1_11.ravel()

b2_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/clip_b2r.tif', gdal.GA_ReadOnly)
b2_11 = b2_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b2_11 = b2_11.ravel()

b3_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/clip_b3r.tif', gdal.GA_ReadOnly)
b3_11 = b3_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b3_11 = b3_11.ravel()

b4_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/clip_b4r.tif', gdal.GA_ReadOnly)
b4_11 = b4_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b4_11 = b4_11.ravel()

b5_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/clip_b5r.tif', gdal.GA_ReadOnly)
b5_11 = b5_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b5_11 = b5_11.ravel()

b7_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/clip_b7r.tif', gdal.GA_ReadOnly)
b7_11 = b7_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
b7_11 = b7_11.ravel()

ndvi_11_ds = gdal.Open('/Volumes/ga87rif/Study Project/satelite images/Level-2/2011/ndvi.tif', gdal.GA_ReadOnly)
ndvi_11 = ndvi_11_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)
ndvi_11 = ndvi_11.ravel()

#stack these bands
img_11 = np.array([b1_11,b2_11,b3_11,b4_11,b5_11,b7_11,ndvi_11])
img_11 = img_11.transpose()

#saving the resulting array into .npy
np.save("/Volumes/ga87rif/Study Project/satelite images/Level-2/img_11.npy", img_11)