import numpy as np
from sklearn.ensemble import RandomForestClassifier 
import pandas
from sklearn.externals import joblib

# 50 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=50, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_50trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_50trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#100 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=100, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_100trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_100trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#200 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=200, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_200trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_200trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#300 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=300, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_300trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_300trees.npy', predict)


#---------------------------------------------------------------------------------------------------------
#400 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=400, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_400trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_400trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#500 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=500, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_500trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_500trees.npy', predict)


#---------------------------------------------------------------------------------------------------------
#750 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=700, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_750trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_750trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
#1000 trees
# Initialize our model with n_estimators trees
rf11 = RandomForestClassifier(n_estimators=1000, oob_score=True)

# Fit our model to training data
rf11 = rf11.fit(td11, class11)

#save model
joblib.dump(rf11, "/Users/aviputripertiwi/Documents/TU Munchen/Study Project/rf11_1000trees.sav")

#predict
predict = rf11.predict(img_11)
np.save('/Volumes/ga87rif/Study Project/Result/New/result11_1000trees.npy', predict)

#---------------------------------------------------------------------------------------------------------
