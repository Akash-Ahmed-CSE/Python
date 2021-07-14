# Enter your code here. Read input from STDIN. Print output to STDOUT
nx = list(map(int, input().split()))
#n, x = nx[0], nx[1]
n = nx[0]
x = nx[1]
z = []
for i in range(x):
    z.append(list(map(float, input().split())))
#print(z)
zipVar = zip(*z)
#print(list(zipVar))
for i in zipVar:
    print(sum(i)/x)
