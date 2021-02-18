name = input("Enter a file:")
if len(name)<1 : name="mbox-short.txt"

file=open(name)
email=dict()
for line in file:
    if not line.startswith("From "): continue
    line=line.split()
    line=line[1]
    email[line]=email.get(line,0)+1
bw=None
bn=None
for word,number in email.items():
    if bn==None or number>bn:
        bn=number
        bw=word
print(bw,bn)
