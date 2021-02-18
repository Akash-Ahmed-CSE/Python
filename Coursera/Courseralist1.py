fname = input("Enter file name: ")
counter = 0
f = open(fname)

for line in f:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    else:
     words = line.split()
     print(words[1])
     counter=counter+1

print("There were", counter, "lines in the file with From as the first word")

