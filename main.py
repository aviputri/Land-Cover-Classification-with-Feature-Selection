import pandas as pd
from simpledbf import Dbf5 #use to read DBF files
from osgeo import gdal, gdal_array, ogr
import struct
import numpy as np
from sklearn.ensemble import RandomForestClassifier 
from sklearn.externals import joblib #use to save the model as .SAV
from sklearn.metrics import accuracy_score, confusion_matrix

# Tell GDAL to throw Python exceptions, and register all drivers
gdal.UseExceptions()
gdal.AllRegister()

#read the class of each data sample
def read_class(tabular_data, gt_array, gt_array_file):

	dbf = Dbf5(tabular_data) # tabular_data = '/location/test.dbf'
	df = dbf.to_dataframe()
	class_id = d['Id'] #[] == __getitem__ syntax
	array = class_id.values
	gt_array = array.ravel()

	# save into .npy
	np.save(gt_array_file, gt_array) #gt_array save = '/location/array.npy'


#extract raster values of each sample point and save it into numpy array
# this extract 1 band
def extract_values(shp, raster, band_array):

	#open raster
	src_ds = gdal.open(raster)
	gt = src_ds.GetGeoTransform()
	rb = src_ds.GetRasterBand(1)

	#open shapefile
	ds = ogr.Open(shp)
	lyr=ds.GetLayer()
	li_values = list()
	for feat in lyr:
		geom = feat.GetGeometryRef()
		mx,my=geom.GetX(), geom.GetY()  #coord in map units

		#Convert from map to pixel coordinates
		#Only works for geotransforms with no rotation
		px = int((mx - gt[0]) / gt[1]) #x pixel
		py = int((my - gt[3]) / gt[5]) #y pixel

		intval=rb.ReadAsArray(px,py,1,1)
		li_values.append([intval[0]])
		a = np.array(li_values)
		b = a.ravel()
		band_array = b.astype(np.uint8)

#combine the bands
def combine_bands(b1, b2, b3, b4, b5, b7, ndvi, multiband_array, multiband_array_file):

	b1 = b1.ravel()
	b2 = b2.ravel()
	b3 = b3.ravel()
	b4 = b4.ravel()
	b5 = b5.ravel()
	b7 = b7.ravel()
	ndvi = ndvi.ravel()
	comb = np.array([b1, b2, b3, b4, b5, b7, ndvi])
	multiband_array = comb.transpose()

	np.save(multiband_array, multiband_array_file)

#import the image band to be predicted (one by one)
def create_band(band, band_array):

	band_ds = gdal.Open(band, gdal.GA_ReadOnly)
	band_array = band_ds.GetRasterBand(1).ReadAsArray().astype(np.float64)

	#then call combine_bands!!

#train the random forest and predict images
def train_rf(trees, minsamples, maxfeatures, train_array, gt_array, model_sav, img, 
	result_array, result_array_file):

	rf = RandomForestClassifier(n_estimators = trees, min_samples_split = 10, 
		max_features = maxfeatures, oob_score=True)

	rf = rf.fit(train_array, gt_array)

	#save model
	joblib.dump(rf, model_sav)

	result = rf.predict(img)

	np.save(result_array, result_array_file)



#make raster file from the result
def rasterize(result_array, result_raster):

	a = result_array.astype(np.uint8)

	#reshape into 2D
	b = np.reshape(a, (-1,3057))
	c = np.flipud(b) #flip vertically
	#because rasterio writes from bottom to top

	#transform = from_origin(110....<--dari origin, -7....<--bukan dari origin, 0.000271658, -0.000271658)
	transform = from_origin(110.0363020639564269, -7.8701315292535803, 0.000271658, -0.000271658)

	new_dataset = rasterio.open(result_raster, 'w', driver='GTiff',
		height = b.shape[0], width = c.shape[1],
		count=1, dtype=c.dtype,
		crs='+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs',
		transform=transform)

	new_dataset.write(c, 1)
	new_dataset.close()
	#then call the extract_values function!!
	#output: test_array

def test_accuracy(year, trees, test_array, gt_test_array):

	a = accuracy_score(gt_test_array, test_array)
	b = confusion_matrix(gt_test_array, test_array, labels=[1,2,3,4,5,6,7,8])

	print(year)
	print 'The overall accuracy of ',trees,' trees is: ',a
	print(b)

