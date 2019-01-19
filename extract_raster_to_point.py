from osgeo import gdal,ogr
import struct

#define raster
src_filename = '/tmp/test.tif'
#define shapefile
shp_filename = '/tmp/test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
for feat in lyr:
    geom = feat.GetGeometryRef()
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    print intval[0] #intval is a numpy array, length=1 as we only asked for 1 pixel value
