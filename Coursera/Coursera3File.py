

fname=input("Enter fiel name :")
file=open(fname)
for line in file:
    print(line.rstrip())