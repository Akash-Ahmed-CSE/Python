n=int(input())
dictionary={}
for i in range(0,n):
    array=input().split()
    marks=list(map(float,array[1:]))
    dictionary[array[0]]= sum(marks)/float(len(marks))
print("%.2f"% dictionary[input()])
