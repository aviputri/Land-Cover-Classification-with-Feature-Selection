from osgeo import gdal,ogr
import struct
import numpy as np

#---------------------------------------------------------------------------------------------------------
#Ground Truth
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Ground Truth Data/clip_data2011.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    gt11 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_gt11.npy', gt11)

#if I need the FID, use this    
#    li_values.append([feat_id, intval[0]])
#    print intval[0] #intval is a numpy array, length=1 as we only asked for 1 pixel value

#---------------------------------------------------------------------------------------------------------
#50 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_50trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_50 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_50.npy', r11_50)


#---------------------------------------------------------------------------------------------------------
#100 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_100trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_100 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_100.npy', r11_100)


#---------------------------------------------------------------------------------------------------------
#200 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_200trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_200 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_200.npy', r11_200)


#---------------------------------------------------------------------------------------------------------
#300 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_300trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_300 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_300.npy', r11_300)


#---------------------------------------------------------------------------------------------------------
#400 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_400trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_400 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_400.npy', r11_400)


#---------------------------------------------------------------------------------------------------------
#500 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_500trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_500 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_500.npy', r11_500)

#---------------------------------------------------------------------------------------------------------
#750 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_750trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_750 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_750.npy', r11_750)

#---------------------------------------------------------------------------------------------------------
#1000 trees
#define raster
src_filename = '/Volumes/ga87rif/Study Project/Result/New/result11_1000trees.tif'
#define shapefile
shp_filename = '/Volumes/ga87rif/Study Project/Samples/s11test.shp'

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
    r11_1000 = b.astype(np.uint8)

np.save('/Volumes/ga87rif/Study Project/Result/New/test_11_1000.npy', r11_1000)
