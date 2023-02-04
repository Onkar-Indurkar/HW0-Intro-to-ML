# -*- coding: utf-8 -*-
"""HW0 ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pjBNlrY2D_sxolKEyuE0DOHl4XiQ9oBI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('D3.csv') or
#df = pd.read_csv('/content/sample_data/D3.csv') #using google collab & uploading d3.csv in sample data folder in files or
df = pd.read_csv('https://raw.githubusercontent.com/Onkar-Indurkar/Intro-to-ML/main/D3.csv')
df.head()        # To get first n rows from the dataset default value of n is 5 
M=len(df)
M

X1 = df.values[:, 0]     # get input values from first column 
Y = df.values[:, 3]      # get output values from second column 
m = len(Y)               # Number of training examples
print('X1 = ', X1[: 10]) # Show only first 10 records print('Y = ', Y[: 10])
print('m = ', m)

X2 = df.values[:, 1]     # get input values from first column 
Y = df.values[:, 3]      # get output values from second column 
m = len(Y)               # Number of training examples
print('X2 = ', X2[: 10]) # Show only first 10 records print('Y = ', Y[: 10])
print('m = ', m)

X3 = df.values[:, 2]     # get input values from first column 
Y = df.values[:, 3]      # get output values from second column 
m = len(Y)               # Number of training examples
print('X3 = ', X3[: 10]) # Show only first 10 records print('Y = ', Y[: 10])
print('m = ', m)

plt.scatter(X1,Y, color='red',marker= '+') 
plt.grid()
plt.rcParams["figure.figsize"] = (10,6) 
plt.xlabel('X1')
plt.ylabel('Y')
plt.title('X1 data')

plt.scatter(X2,Y, color='green',marker= '+') 
plt.grid()
plt.rcParams["figure.figsize"] = (10,6) 
plt.xlabel('X2')
plt.ylabel('Y')
plt.title('X2 data')

plt.scatter(X3,Y, color='blue',marker= '+') 
plt.grid()
plt.rcParams["figure.figsize"] = (10,6) 
plt.xlabel('X3')
plt.ylabel('Y')
plt.title('X3 data')

#Lets create a matrix with single column of ones
X_0 = np.ones((m, 1)) 
X_0[:5]

"""X1"""

X_1 = X1.reshape(m, 1) 
X_1[:10]

# Lets use hstack() function from numpy to stack X_0 and X_1 horizontally (i.e. colum # This will be our final X matrix (feature matrix)
X1 = np.hstack((X_0, X_1))
X1[:10]

theta_1 = np.zeros(2) 
theta_1

def compute_cost_1(X1, Y, theta_1): 
  predictions_1 = X1.dot(theta_1) 
  errors_1 = np.subtract(predictions_1, Y) 
  sqrErrors_1 = np.square(errors_1)
  J1 = (1 / (2 * m)) * np.sum(sqrErrors_1) 
  return J1

cost_1 = compute_cost_1(X1, Y, theta_1)
print('The cost for given values of theta_1 =', cost_1)

def gradient_descent_1(X1, Y, theta_1, alpha_1, iterations_1):
  cost_history_1 = np.zeros(iterations_1)
  for i in range(iterations_1):
    predictions_1 = X1.dot(theta_1)
    errors_1 = np.subtract(predictions_1, Y)
    sum_delta_1 = (alpha_1 / m) * X1.transpose().dot(errors_1); theta_1 = theta_1 - sum_delta_1;
    cost_history_1[i] = compute_cost_1(X1, Y, theta_1)
  return theta_1, cost_history_1

theta_1 = [0., 0.] 
iterations_1 = 1500; 
alpha_1 = 0.01;

theta_1, cost_history_1 = gradient_descent_1(X1, Y, theta_1, alpha_1, iterations_1) 
print('Final value of theta =', theta_1)
print('cost_history =', cost_history_1[-1])

# Since X is list of list (feature matrix) lets take values of column of index 1 only
plt.scatter(X1[:,1], Y, color='green', marker= '+', label= 'Training Data') 
plt.plot(X1[:,1],X1.dot(theta_1), color='red', label='Linear Regression')

plt.rcParams["figure.figsize"] = (10,6) 
plt.grid()
plt.xlabel('X1')
plt.ylabel('Y')
plt.title('Linear Regression Model for X1') 
plt.legend()

plt.plot(range(1, iterations_1 + 1),cost_history_1, color='blue') 
plt.rcParams["figure.figsize"] = (10,6)
plt.grid()
plt.xlabel('Number of iterations') 
plt.ylabel('Cost (J1)') 
plt.title('Convergence of gradient descent for X1')

"""X2"""

X_2 = X2.reshape(m, 1) 
X_2[:10]

# Lets use hstack() function from numpy to stack X_0 and X_1 horizontally (i.e. colum 
# This will be our final X matrix (feature matrix)
X2 = np.hstack((X_0, X_2))
X2[:10]

theta_2 = np.zeros(2) 
theta_2

def compute_cost_2(X2, Y, theta_2): 
  predictions_2 = X2.dot(theta_2) 
  errors_2 = np.subtract(predictions_2, Y) 
  sqrErrors_2 = np.square(errors_2)
  J2 = (1 / (2 * m)) * np.sum(sqrErrors_2) 
  return J2

cost_2 = compute_cost_2(X2, Y, theta_2)
print('The cost for given values of theta_2 =', cost_2)

def gradient_descent_2(X2, Y, theta_2, alpha_2, iterations_2):
  cost_history_2 = np.zeros(iterations_2)
  for i in range(iterations_2):
    predictions_2 = X2.dot(theta_2)
    errors_2 = np.subtract(predictions_2, Y)
    sum_delta_2 = (alpha_2 / m) * X2.transpose().dot(errors_2); theta_2 = theta_2 - sum_delta_2;
    cost_history_2[i] = compute_cost_2(X2, Y, theta_2)
  return theta_2, cost_history_2

theta_2 = [0., 0.] 
iterations_2 = 1500; 
alpha_2 = 0.01;

theta_2, cost_history_2 = gradient_descent_2(X2, Y, theta_2, alpha_2, iterations_2) 
print('Final value of theta =', theta_2)
print('cost_history =', cost_history_2[-1])

# Since X is list of list (feature matrix) lets take values of column of index 1 only
plt.scatter(X2[:,1], Y, color='green', marker= '+', label= 'Training Data') 
plt.plot(X2[:,1],X2.dot(theta_2), color='red', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6) 
plt.grid()
plt.xlabel('X2')
plt.ylabel('Y')
plt.title('Linear Regression Model for X2') 
plt.legend()

plt.plot(range(1, iterations_2 + 1),cost_history_2, color='blue') 
plt.rcParams["figure.figsize"] = (10,6)
plt.grid()
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J2)') 
plt.title('Convergence of gradient descent')

"""X3"""

X_3 = X3.reshape(m, 1) 
X_3[:10]

# Lets use hstack() function from numpy to stack X_0 and X_1 horizontally (i.e. colum 
# This will be our final X matrix (feature matrix)
X3 = np.hstack((X_0, X_3))
X3[:10]

theta_3 = np.zeros(2) 
theta_3

def compute_cost_3(X3, Y, theta_3): 
  predictions_3 = X3.dot(theta_3) 
  errors_3 = np.subtract(predictions_3, Y) 
  sqrErrors_3 = np.square(errors_3)
  J3 = (1 / (2 * m)) * np.sum(sqrErrors_3) 
  return J3

cost_3 = compute_cost_3(X3, Y, theta_3)
print('The cost for given values of theta_3 =', cost_3)

def gradient_descent_3(X3, Y, theta_3, alpha_3, iterations_3): 
  cost_history_3 = np.zeros(iterations_3)
  for i in range(iterations_3):
    predictions_3 = X3.dot(theta_3)
    errors_3 = np.subtract(predictions_3, Y)
    sum_delta_3 = (alpha_3 / m) * X3.transpose().dot(errors_3); theta_3 = theta_3 - sum_delta_3;
    cost_history_3[i] = compute_cost_3(X3, Y, theta_3)
  return theta_3, cost_history_3

theta_3 = [0., 0.] 
iterations_3 = 1500; 
alpha_3 = 0.01;

theta_3, cost_history_3 = gradient_descent_3(X3, Y, theta_3, alpha_3, iterations_3) 
print('Final value of theta =', theta_3)
print('cost_history =', cost_history_3[-1])

# Since X is list of list (feature matrix) lets take values of column of index 1 only
plt.scatter(X3[:,1], Y, color='green', marker= '+', label= 'Training Data') 
plt.plot(X3[:,1],X3.dot(theta_3), color='red', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6) 
plt.grid()
plt.xlabel('X3')
plt.ylabel('Y')
plt.title('Linear Regression Model for X3') 
plt.legend()

plt.plot(range(1, iterations_3 + 1),cost_history_3, color='blue') 
plt.rcParams["figure.figsize"] = (10,6)
plt.grid()
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J3)') 
plt.title('Convergence of gradient descent')

"""For Q2-4"""

X = df.values[:, (0,1,2)]  # get input values from first column
y = df.values[:, 3]        # get output values from 4th column 
m = len(y)                 # Number of training examples
print('X = ', X[: 10])     # Show only first 10 records
print('y = ', y[: 10])
print('m = ', m)

X_0 = np.ones((m, 1)) 
X_0[:5]

# Using reshape function convert X 1D array to 2D array of dimension 97x1
X_N = X.reshape(m, 3) 
X_N[:10]

X = np.hstack((X_0, X_N)) 
X[:5]

theta = np.zeros(4) 
theta

def compute_cost(X, y, theta): 
  predictions = X.dot(theta)
  errors = np.subtract(predictions, y)
  sqrErrors = np.square(errors)
  J = 1 / (2 * m) * np.sum(sqrErrors) 
  return J

cost = compute_cost(X, y, theta)
print('The cost for given values of theta_0 and theta_1 =', cost)

def gradient_descent(X, y, theta, alpha, iterations): 
  cost_history = np.zeros(iterations)
  for i in range(iterations):
    predictions = X.dot(theta)
    errors = np.subtract(predictions, y)
    sum_delta = (alpha / m) * X.transpose().dot(errors); theta = theta - sum_delta;
    cost_history[i] = compute_cost(X, y, theta)
  return theta, cost_history

theta = [0., 0., 0., 0.] 
iterations = 1500; 
alpha = 0.01;

theta, cost_history = gradient_descent(X, y, theta, alpha, iterations) 
print('Final value of theta =', theta)
print('cost_history =', cost_history[-1])

# Since X is list of list (feature matrix) lets take values of column of index 1 only
plt.scatter(X[:,1], y, color='green', marker= '+', label= 'Training Data') 
plt.plot(X[:,1],X.dot(theta), color='red', label='Linear Regression')
plt.rcParams["figure.figsize"] = (10,6) 
plt.grid()
plt.xlabel('Population of City in 10,000s') 
plt.ylabel('Profit in $10,000s') 
plt.title('Linear Regression Fit for q2 part 4') 
plt.legend()

plt.plot(range(1, iterations + 1),cost_history, color='blue') 
plt.rcParams["figure.figsize"] = (10,6)
plt.grid()
plt.xlabel('Number of iterations')
plt.ylabel('Cost (J)') 
plt.title('Convergence of gradient descent')

#Predicting values for Y
sum_1 = theta[3]*(1) + theta[2]*(1) + theta[1]*(1) + theta[0] 
sum_2 = theta[3]*(2) + theta[2]*(0) + theta[1]*(4) + theta[0] 
sum_3 = theta[3]*(3) + theta[2]*(2) + theta[1]*(1) + theta[0]

print(sum_1)
print(sum_2)
print(sum_3)