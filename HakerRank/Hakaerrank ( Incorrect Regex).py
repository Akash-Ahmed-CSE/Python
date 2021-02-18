import re

n=int(input())
for i in range(n):
    ans = True
    try:
        reg=re.compile(input())

    except:
        ans=False
    print(ans)
