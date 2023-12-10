import numpy as np

# Define dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

# Calculate means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate slope (m) and y-intercept (c)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator
c = y_mean - m * x_mean

# Define a function for prediction
def predict(x):
    return m * x + c

# Make predictions on a test set
test = np.array([12, 13])
pred_y = predict(test)
#pred_y = m * test + c

# Print the predicted values
print(pred_y)
