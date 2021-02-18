import matplotlib.pyplot as plt
import numpy as np

years = np.array([2014,2015])
data = np.array([[17348.1,17947.0],[10430.7,10982.8],[4596.2,4123.3],[3874.4,3357.6],[2991.7,2849.3],[2833.7,2421.6],[2042.6,2090.7],[2141.9,1815.8]])
countries = ['US','China','Japan','Germany','UK','France','India','Italy']

cnum = np.arange(len(countries))

change = 100.0 * (data[:,1] -data[:,0])/data[:,0]
print(change)

plt.figure()
plt.bar(cnum,change)

ticks= plt.xticks(cnum,countries)
plt.title('2015 Echonomic Change')
plt.xlabel('Country')
plt.ylabel('GDP changes')



data14 = data[:,0]
cat9 = 77960- np.sum(data14)
data14 = np.append(data14,cat9)
countries8=countries
countries8.append('other')
plt.figure()
plt.pie(data14,labels=countries,autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()





