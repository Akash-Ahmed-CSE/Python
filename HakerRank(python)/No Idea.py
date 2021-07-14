# Enter your code here. Read input from STDIN. Print output to STDOUT

n,m = map(int, input().split()) #first two values are a string we just have to split thema nd put them in n and m value

arr = list(map(int,input().split()))
happniness = 0
A = set(map(int, input().split()))
B = set(map(int, input().split()))
for i in arr:
    if i in A:
        happniness+=1
    elif i in B:
        happniness-=1
print(happniness)
