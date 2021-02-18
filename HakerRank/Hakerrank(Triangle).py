
for i in range(1,int(input())):
    sum = sum+10**i
    print(i*((1+sum)%10**i))