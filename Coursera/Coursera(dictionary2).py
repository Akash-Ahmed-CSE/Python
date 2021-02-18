counts=dict()
co=dict()
names=['akash','rana','akash','rony','rana','akash','rony','pritom','rana']

for name in names:
    if name not in counts:
      counts[name]=1
    else:
        counts[name]=counts[name]+1

print(counts)
#same thing using get methods
for name in names:
    co[name]=co.get(name,0)+1

print(co)