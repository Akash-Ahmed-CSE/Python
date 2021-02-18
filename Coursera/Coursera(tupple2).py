fhand = open("read.txt")
counts=dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

a=sorted([( v,k) for k,v in  counts.items()],reverse=True)
print(a)

for val,key in a[:10]:
    print(key,val)