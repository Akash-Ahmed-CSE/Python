import re

n = int(input())
pattern = r'^[+-]?[0-9]*\.[0-9]+$'
for i in range(n):
    s = input()
    print(bool(re.match(pattern,s)))








