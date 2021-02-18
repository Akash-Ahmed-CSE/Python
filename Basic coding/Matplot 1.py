import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]


plt.plot(x,y,label='fig 1 ')
plt.plot(x2,y2,label='fig2')

plt.xlabel("Plot number:")
plt.ylabel("interest graph")
plt.grid(True)
plt.title('Interesting Graph\nOutput')
plt.legend()
plt.show()


