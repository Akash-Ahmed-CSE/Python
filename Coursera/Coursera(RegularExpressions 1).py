import re
x ='My name is 123. i am 19 years. i have 12 banana'
y=re.findall('[0-9]+',x)
print(y)
p=re.findall('[AEIOUM]',x)
print(p)
hand=open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)