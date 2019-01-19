import pandas as pd 
import numpy as np 

# Digital Numbers
# df = dataframe
# this is pandas tabular data
td09_df = pd.read_excel('/Volumes/ga87rif/Study Project/Samples/trainingsample.xlsx', sheet_name = "2009", usecols = "E:K", header = 0)

#convert into numpy array
td09 = td09_df.values

#saving the resulting array into .npy
f09 = '/Volumes/ga87rif/Study Project/Samples/td09.npy'
np.save(f09, td09)

# Feature Classes
class09_df = pd.read_excel('/Volumes/ga87rif/Study Project/Samples/trainingsample.xlsx', sheet_name = "2009", usecols = "B", header = 0)

#convert into numpy array
class09 = class09_df.values
class09 = class09.ravel()

#saving the resulting array into .npy
c09 = '/Volumes/ga87rif/Study Project/Samples/class09.npy'
np.save(c09, class09)