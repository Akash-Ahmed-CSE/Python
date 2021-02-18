# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    line=line.split()

    for a in line:
        if a in lst:
            continue
        else:
            lst.append(a)

lst.sort()
print(lst)




