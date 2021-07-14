# Enter your code here. Read input from STDIN. Print output to STDOUT
l= input()

for _ in range(int(l)):
    a,b = input().split()
    try:
        c = (int(a)// int(b))
        print(c)
    except Exception as e:
        print('Error Code: '+str(e))
