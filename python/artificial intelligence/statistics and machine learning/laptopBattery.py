# Laptop Battery Life
## https://www.hackerrank.com/challenges/battery/problem

import sys
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
from sklearn import linear_model

training = []
with open('trainingdata.txt') as inputfile:
    for line in inputfile:
        training.append(list(map(float,line.strip().split(','))))
        
trainingArray = np.array(training)
        
trainingX = trainingArray[:,0].reshape(-1, 1)
trainingY = trainingArray[:,1].reshape(-1, 1)

plt.scatter(trainingX, trainingY,  color='black')

trainingX = trainingArray[trainingArray[:,0] <= 4.00][:,0].reshape(-1,1)
trainingY = trainingArray[trainingArray[:,0] <= 4.00][:,1].reshape(-1,1)

regr = linear_model.LinearRegression()
regr.fit(trainingX, trainingY)

x = float(input().strip())
prediction = regr.predict(x)
print(float("{0:.2f}".format(prediction[0][0])) if x < 4.0 else 8.00)
