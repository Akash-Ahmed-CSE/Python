strings = []
queries = []
n = int(input())
for i in range(n):
    j = input()
    strings.append(j)
q = int(input())
for i in range(q):
    j = input()
    queries.append(j)


for i in range(len(queries)):
    c = 0
    for j in range(len(strings)):
        if queries[i] == strings[j]:
            c+=1
    print(c)





