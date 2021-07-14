s = []
m = []
for i in range(int(input())):
    name = input()
    grade = float(input())
    s +=[[name,grade]]
    m+=[grade]
sl = (sorted(set(m)))[1]
for i,j in sorted((s)):
    if j==sl:
        print(i)
