name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emcount = dict()

for line in handle:
    if not line.startswith("From "): continue
    line = line.split()
    line = line[1]
    emcount[line] = emcount.get(line, 0) +1
bigcount = None
bigword = None
for word,count in emcount.items():
 if bigcount == None or count > bigcount:
    bigcount = count
    bigword = word
print(bigword, bigcount)
