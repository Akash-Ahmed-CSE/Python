import re

h = open("tt.txt")
x=list()
for l in h:
     y = re.findall('[0-9]+',l)
     x = x+y
s=0
for z in x:
    s = s + int(z)

print(s)