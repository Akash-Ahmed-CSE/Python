n = int(input())
s1 = set(map(int,input().split()))
m = int(input())
s2 = set(map(int,input().split()))

s3 = s1.union(s2)
l = []
for i in s3:
    if i in s1 and i in s2:
        pass
    else:
     l.append(i)

l.sort()
for i in l:
    print(i)