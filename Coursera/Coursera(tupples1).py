fhand = open("read.txt")
counts=dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
list=list()
for key,val in counts.items():
    newtup=(val,key)
    list.append(newtup)
list=sorted(list,reverse= True)

for val,key in list[:10]:
    print(key,val)
