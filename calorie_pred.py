import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor,XGBClassifier
import joblib
import catboost as cb
import joblib

params = {
    'task': 'train', 
    'boosting': 'gbdt',
    'objective': 'regression',
    'num_leaves': 10,
    'learnnig_rage': 0.05,
    'metric': {'l2','l1'},
    'verbose': -1
}
df = pd.read_csv('datasets/exercise_dataset.csv')


X = df[['205 lb']]
y = df[['Activity, Exercise or Sport (1 hour)']]

print(X)
print(y)

enc = LabelEncoder()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
y_train,y_test = enc.fit_transform(y_train), enc.fit_transform(y_test)

y_train = y_train.ravel()
train_y = np.array(y_train).astype(int)

train_dataset = cb.Pool(X_train, train_y) 
test_dataset = cb.Pool(X_test, y_test)

clf = cb.CatBoostRegressor(loss_function='RMSE')
grid = {'iterations': [100, 150, 200],
        'learning_rate': [0.03, 0.1],
        'depth': [2, 4, 6, 8],
        'l2_leaf_reg': [0.2, 0.5, 1, 3]
        }
clf.grid_search(grid, train_dataset)


y_pred = clf.predict(X_test)

np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

score = mean_squared_error(y_test,y_pred)
print(score)

filename = '205weightModel.sav'
joblib.dump(clf, filename)