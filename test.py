#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier  
from sklearn.metrics import classification_report 
import pandas as pd

file = 'log3.csv'
data = pd.read_csv('log3.csv')  

print("-------------------------------------")
print(data.head())

X = data.drop('Label', axis=1).values
y = data['Label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)  
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)  
mlp.fit(X_train, y_train)

testY = 1
testX = 11.3
predict = mlp.predict([[testY, testX]])
predictEval = mlp.predict(X_test)

print("-------------------------------------")
print("Accuracy: ",mlp.score(X_test, y_test))
print("Caso --> Color = ", testY, "/ Distancia = ", testX )
print("Prediction: ", predict[0])
print("-------------------------------------")
print('MLP:\n')
print(classification_report(predictEval, y_test))