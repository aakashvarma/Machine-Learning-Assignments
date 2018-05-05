# Load CSV file using standard CSV library

import csv
import numpy as np
import pandas as pd
filename = 'diabetes.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
df = pd.DataFrame(x)
print(df.shape)
print(df.head())




























































