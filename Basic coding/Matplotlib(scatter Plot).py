import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,100,20)
y = np.random.randint(1,100,20)
x2 = np.random.randint(1,100,20)
y2 = np.random.randint(1,100,20)

plt.figure(figsize= (6,4))

plt.scatter(x,y,label="First",
            c="b",s=250,
            marker="^")

plt.scatter(x2,y2,label="Second",
            c="orange",
            s=250,marker="s")

plt.xlabel("X",fontsize =15)
plt.ylabel("Y",fontsize= 15)

plt.xticks(size=12)
plt.yticks(size = 12)


plt.title("color scatter Plot!\n 2020",fontsize=18)

plt.legend()
plt.show()
