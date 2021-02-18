name = input("Enter a file:")
if len(name) < 1 : name = "mbox-short.txt"
email=open(name)
d=dict()
for line in email:
    if not line.startswith("From "):continue

    line=line.split()
    line=line[5]
    line=line[0:2]
    d[line]=d.get(line,0)+1

lst=list()
for v,k in d.items():
    lst.append((v,k))


lst.sort()
for v,k in lst:
    print(v,k)
