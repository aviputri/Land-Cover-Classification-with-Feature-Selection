import pandas as pd 
import numpy as np 

# Digital Numbers
# df = dataframe
# this is pandas tabular data
td11_df = pd.read_excel('/Volumes/ga87rif/Study Project/Samples/trainingsample.xlsx', sheet_name = "2011", usecols = "E:K", header = 0)

#convert into numpy array
td11 = td11_df.values

#saving the resulting array into .npy
np.save('/Volumes/ga87rif/Study Project/Samples/td11.npy', td11)

# Feature Classes
class11_df = pd.read_excel('/Volumes/ga87rif/Study Project/Samples/trainingsample.xlsx', sheet_name = "2011", usecols = "B", header = 0)

#convert into numpy array
class11 = class11_df.values
class11 = class11.ravel()

#saving the resulting array into .npy
np.save('/Volumes/ga87rif/Study Project/Samples/class11.npy', class11)