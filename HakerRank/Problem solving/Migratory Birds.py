n = int(input())

birds = list(map(int, input().split()))

coutns = [0]*n #[000]

for i in birds:
    coutns[i]+= 1


#print(birds)
#print(coutns)


print(coutns.index(max(coutns)))














