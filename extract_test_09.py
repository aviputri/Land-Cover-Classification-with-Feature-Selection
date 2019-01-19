from osgeo import gdal,ogr
import struct
import numpy as np

#---------------------------------------------------------------------------------------------------------
#Ground Truth
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Ground Truth Data/clip_data2009.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([feat_id, intval[0]])
    a = np.array(li_values)
    b = a[:,1]
    c = b.ravel()
    gt09 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_gt09.npy', gt09)

#if I need the FID, use this    
#    li_values.append([feat_id, intval[0]])
#    print intval[0] #intval is a numpy array, length=1 as we only asked for 1 pixel value

#---------------------------------------------------------------------------------------------------------
#50 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_50trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([feat_id, intval[0]])
    a = np.array(li_values)
    b = a[:,1]
    c = b.ravel()
    r09_50 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_50.npy', r09_50)


#---------------------------------------------------------------------------------------------------------
#100 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_100trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_100 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_100.npy', r09_100)


#---------------------------------------------------------------------------------------------------------
#200 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_200trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_200 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_200.npy', r09_200)


#---------------------------------------------------------------------------------------------------------
#300 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_300trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_300 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_300.npy', r09_300)


#---------------------------------------------------------------------------------------------------------
#400 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_400trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_400 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_400.npy', r09_400)


#---------------------------------------------------------------------------------------------------------
#500 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_500trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_500 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_500.npy', r09_500)

#---------------------------------------------------------------------------------------------------------
#750 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_750trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_750 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_750.npy', r09_750)

#---------------------------------------------------------------------------------------------------------
#1000 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result09_1000trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s09test.shp'

#open raster
src_ds=gdal.Open(src_filename) 
gt=src_ds.GetGeoTransform()
rb=src_ds.GetRasterBand(1)

#open shapefile
ds=ogr.Open(shp_filename)
lyr=ds.GetLayer()
li_values = list()
for feat in lyr:
    geom = feat.GetGeometryRef()
#    feat_id = feat.GetField('FID')
    mx,my=geom.GetX(), geom.GetY()  #coord in map units

    #Convert from map to pixel coordinates.
    #Only works for geotransforms with no rotation.
    px = int((mx - gt[0]) / gt[1]) #x pixel
    py = int((my - gt[3]) / gt[5]) #y pixel

    intval=rb.ReadAsArray(px,py,1,1)
    li_values.append([intval[0]])
    a = np.array(li_values)
    b = a.ravel()
    r09_1000 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_09_1000.npy', r09_1000)
