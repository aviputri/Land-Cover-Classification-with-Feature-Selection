import numpy as np
from sklearn.ensemble import RandomForestClassifier 
import pandas
from sklearn.externals import joblib

# 50 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=50, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_50trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_50trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#100 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=100, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_100trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_100trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#200 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=200, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_200trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_200trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#300 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=300, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_300trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_300trees.npy', predict)


#---------------------------------------------------------------------------------------------------------
#400 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=400, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_400trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_400trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#500 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=500, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_500trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_500trees.npy', predict)


#---------------------------------------------------------------------------------------------------------
#750 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=700, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_750trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_750trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#1000 trees
# Initialize our model with n_estimators trees
rf = RandomForestClassifier(n_estimators=1000, oob_score=True)

# Fit our model to training data
rf = rf.fit(td09, class09)

#save model
joblib.dump(rf, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf_1000trees.sav")

#predict
predict = rf.predict(img_09)
np.save('/Volumes/ga87rif/Study Project/Result/New/result09_1000trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
