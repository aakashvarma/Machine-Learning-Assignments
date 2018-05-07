# Load CSV file using standard CSV library

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
filename = 'diabetes.csv'
raw_data = open(filename, 'r')
reader = csv.reader(raw_data, delimiter = ',', quoting = csv.QUOTE_NONE)
x = list(reader)
df = pd.DataFrame(x)

# Renaming header
df.columns = df.iloc[0]
df = df[1:]

# Convert 'object datatype to 'numeric (float)' datatype
df = df.apply(pd.to_numeric, downcast = 'float', errors='ignore')

# Data dimensions
print (df.shape)

# Data types
print(df.dtypes)

# Descriptive Statistics_________________
print (df.describe())

# Correlation
print (df.corr(method = 'pearson'))

# Skewness
print (df.skew())

# UNIVARIATE PLOTS________________________

# Histograms
plt.hist(df)
plt.show()

# Density Plots
# df.plot(kind = 'density', subplots = True, layout = (3,3), sharex = False)
# pyplot.show()





















































