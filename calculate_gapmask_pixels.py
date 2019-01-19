# Import GDAL, NumPy, and matplotlib
from osgeo import gdal, gdal_array
import numpy as np
import scipy

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

pixel_ds = gdal.Open('/Volumes/ga87rif/Study Project/countpixel2011.tif', gdal.GA_ReadOnly)
pixel = pixel_ds.GetRasterBand(1).ReadAsArray().astype(np.uint8)
pixel_count = pixel[pixel != -0]

pixel_count.shape

#result: pixel_count.shape = (5072226,)