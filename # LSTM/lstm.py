# Basic (Perceptron) Neural Networks

"""
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

np.random.seed(7)
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter=",")

X = dataset[:,0:8]
Y = dataset[:,8]

model = Sequential()
model.add(Dense(12, input_dim = 8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs = 150, batch_size = 10)

scores = model.evaluate(X, Y)
print ("\n%s: %.2f%%", (model.metrics_names[1], scores[1]*100))

"""

# LSTM - Text generation from Adventuresof machinelearning

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

filename = "something.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
print ("Total Charaterts: ", n_chars)
print ("Total Vocab: ", n_vocab)












