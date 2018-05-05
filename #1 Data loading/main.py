# Load CSV file using standard CSV library

import csv
import numpy as np
import pandas as pd
filename = 'diabetes.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
df = pd.DataFrame(x)

# Renaming header
df.columns = df.iloc[0]
df = df[1:]

# Data dimensions
print (df.shape)

# Data types
print(df.dtypes)

# Descriptive Statistics
print (df.describe())

# Correlation
print (df.corr(method = 'pearson'))




























































