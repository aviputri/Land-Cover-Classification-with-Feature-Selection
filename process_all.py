import main

#-----------------------------------------------------------------------------------------------
# read all train and test sample points

#2009
#0.1 percent sample data
#train
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.1percent/s09train.dbf', 
	gt_array=train09_01, gt_array_file='/Volumes/ga87rif/Study Project/Samples/train09_01.npy')
#test
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.1percent/s09test.dbf',
	gt_array=test09_01, gt_array_file='/Volumes/ga87rif/Study Project/Samples/test09_01.npy')

#0.25 percent sample data
#train
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.25percent/s09train.dbf', 
	gt_array=train09_025, gt_array_file='/Volumes/ga87rif/Study Project/Samples/train09_025.npy')
#test
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.25percent/s09test.dbf',
	gt_array=test09_025, gt_array_file='/Volumes/ga87rif/Study Project/Samples/test09_025.npy')

#0.5 percent sample data
#train
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.5percent/s09train.dbf', 
	gt_array=train09_05, gt_array_file='/Volumes/ga87rif/Study Project/Samples/train09_05.npy')
#test
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.5percent/s09test.dbf',
	gt_array=test09_05, gt_array_file='/Volumes/ga87rif/Study Project/Samples/test09_05.npy')

#2011
#0.1 percent sample data
#train
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.1percent/s11train.dbf', 
	gt_array=train11_01, gt_array_file='/Volumes/ga87rif/Study Project/Samples/train11_01.npy')
#test
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.1percent/s11test.dbf',
	gt_array=test11_01, gt_array_file='/Volumes/ga87rif/Study Project/Samples/test11_01.npy')

#0.25 percent sample data
#train
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.25percent/s11train.dbf', 
	gt_array=train11_025, gt_array_file='/Volumes/ga87rif/Study Project/Samples/train11_025.npy')
#test
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.25percent/s11test.dbf',
	gt_array=test11_025, gt_array_file='/Volumes/ga87rif/Study Project/Samples/test11_025.npy')

#0.5 percent sample data
#train
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.5percent/s11train.dbf', 
	gt_array=train11_05, gt_array_file='/Volumes/ga87rif/Study Project/Samples/train11_05.npy')
#test
read_class(tabular_data='/Volumes/ga87rif/Study Project/Samples/0.5percent/s11test.dbf',
	gt_array=test11_05, gt_array_file='/Volumes/ga87rif/Study Project/Samples/test11_05.npy')

#-----------------------------------------------------------------------------------------------
#read raster values and combine then into train_array

extract_values(shp = , raster, band_array)