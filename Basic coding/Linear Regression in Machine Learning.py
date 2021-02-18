import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('car driving risk analysis.csv')
#print(df)
x = df[['speed']]
y = df['risk']

#print(df.head(5))
#print(df.shape)
#print(df.isnull().any())
#print(x)
#print(y)

#plt.scatter(df['speed'],df['risk'])
#plt.show()

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.60, random_state=1)
#print(xtrain)
#print(xtest)
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(xtrain,ytrain)
#print(reg.predict(xtest))

plt.scatter(df['speed'],df['risk'])
plt.plot(df.speed, reg.predict(df[["speed"]]))
plt.show()

print(reg.predict([[300]]))
print(reg.coef_)
print(reg.intercept_)



