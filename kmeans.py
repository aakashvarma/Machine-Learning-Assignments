from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv"
c = pd.read_csv(url)

# print (c.head())

sepal_length = c.iloc[:,0]
sepal_width = c.iloc[:,1]
petal_length = c.iloc[:,2]
petal_width = c.iloc[:,3]

# plt.scatter(sepal_length,sepal_width,color='red')
# plt.show()

# plt.scatter(petal_length,petal_width,color="blue")
# plt.show()

X = c.iloc[:,0:1]
kmeans = KMeans(n_clusters=4 , random_state=0).fit(X)
print (kmeans.labels_)

# A=np.array([1,1.5,3,5,3.5,4.5,3.5])
# B=np.array([1,2,4,7,5,5,4.5])

# for i in A:
#     print (i)
# print (np.sqrt(A))

# print (A.dot(B))
# print (np.add(A,B))
# print (np.dot(A,B))

# for i,j in zip(A,B):
#     print ("%d , %d" %(i,j))

# print (dict(zip(A,B)))
# print (zip(A,B))

# X=list(zip(A,B))
# X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
# kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
# print (kmeans.labels_)
# print (X)
# C = np.array(X)
# print (C)

# ## This is for plotting the scatter plot
# x=C[:,0]
# y=C[:,1]
# plt.scatter(x,y)
# plt.show()         


# kmeans = KMeans(n_clusters=2, random_state=0).fit(C)
# print (kmeans.labels_)
































