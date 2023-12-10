#define dataset
import numpy as np
x = np.array([[1],[2],[3],[4],[5]])
y = np.array([6,7,8,9,10])

#model import
from sklearn.linear_model import LinearRegression

#assign variable
model = LinearRegression() 

#model.fit #for training 
model.fit(x,y)

#prediction
test = np.array([[12],[13]])
pred_y = model.predict(test)
print(pred_y)