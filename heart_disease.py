# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pickle
hf= pd.read_csv('F:\C\Downloads\heart_failure.csv')
columns=[ 'serum_sodium','ejection_fraction','serum_creatinine','age']
X= hf[columns]
y= hf['DEATH_EVENT']
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2, random_state=7)
dt = DecisionTreeClassifier(max_leaf_nodes=5, random_state=1)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)
dt_acc = accuracy_score(y_test, dt_pred)
print("Decision Tree Claasifier Prediction Rate :", "{:.2f}%".format(100*dt_acc))
filepath = r'C:\Users\prachi\.spyder-py3\model.pkl'
pickle.dump(dt,open(filepath,'wb'))