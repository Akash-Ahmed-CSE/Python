import matplotlib.pyplot as plt
x = [2,4,6,8,10]
y = [6,7,8,2,4]

plt.bar(x,y,label='bars1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('interestingGraph\nCheak Output')
plt.legend()
plt.show()