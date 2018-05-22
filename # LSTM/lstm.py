# Simple Neural Networks

from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(7)
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]

















