import math

a = 1
sum = 0
for i in range(1, 100 + 1):
    sum = sum + (pow(i,3) * (math.factorial(i)))
print(sum)