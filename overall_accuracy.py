import numpy as np 
from sklearn.metrics import accuracy_score, confusion_matrix

#if I need to load the arrays
gt09 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_gt09.npy')
r09_50 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_50.npy')
r09_100 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_100.npy')
r09_200 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_200.npy')
r09_300 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_300.npy')
r09_400 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_400.npy')
r09_500 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_500.npy')
r09_750 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_750.npy')
r09_1000 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_09_1000.npy')

#if I need to load the arrays
gt11 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_gt11.npy')
r11_50 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_50.npy')
r11_100 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_100.npy')
r11_200 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_200.npy')
r11_300 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_300.npy')
r11_400 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_400.npy')
r11_500 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_500.npy')
r11_750 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_750.npy')
r11_1000 = np.load('/Volumes/ga87rif/Study Project/Result/New/test_11_1000.npy')

#accuracy_score(y_true, y_pred)
a = accuracy_score(gt09, r09_50)
b = accuracy_score(gt09, r09_100)
c = accuracy_score(gt09, r09_200)
d = accuracy_score(gt09, r09_300)
e = accuracy_score(gt09, r09_400)
f = accuracy_score(gt09, r09_500)
g = accuracy_score(gt09, r09_750)
h = accuracy_score(gt09, r09_1000)

print '50 trees: ',a,'\n100 trees: ',b,'\n200 trees: ', c,'\n300 trees: ', d,'\n400 trees: ', e,'\n500 trees: ', f,'\n750 trees: ', g,'\n1000 trees: ', h

a = accuracy_score(gt11, r11_50)
b = accuracy_score(gt11, r11_100)
c = accuracy_score(gt11, r11_200)
d = accuracy_score(gt11, r11_300)
e = accuracy_score(gt11, r11_400)
f = accuracy_score(gt11, r11_500)
g = accuracy_score(gt11, r11_750)
h = accuracy_score(gt11, r11_1000)

print '50 trees: ',a,'\n100 trees: ',b,'\n200 trees: ', c,'\n300 trees: ', d,'\n400 trees: ', e,'\n500 trees: ', f,'\n750 trees: ', g,'\n1000 trees: ', h


#confusion_matrix(y_true, y_pred, labels=None, sample_weight=None)
a = confusion_matrix(gt09, r09_50, labels=[1,2,3,4,5,6,7,8])
print(a)