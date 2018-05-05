# Load CSV file using standard CSV library

import csv
import numpy as np
filename = 'diabetes.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
data = np.array(x)
print(data.shape)





























































