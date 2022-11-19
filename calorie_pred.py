import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt

#Make 4 seperate models for each weight category and package them to joblib for backend

df = pd.read_csv('datasets/exercise_dataset.csv')

X = df.loc[:, ['130 lb']]
y = df.loc[:, ['Activity, Exercise or Sport (1 hour)']]

print(y)

enc = OneHotEncoder(handle_unknown='ignore')

dum_df = pd.get_dummies(y, columns=["Activity, Exercise or Sport (1 hour)"], prefix=["Type_is"] )
print(dum_df)