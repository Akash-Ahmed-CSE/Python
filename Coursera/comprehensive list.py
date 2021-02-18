
num= [1,2,3,4,5]
result = [x*x for x in num]
print(result)

x = list(filter(lambda x :x<16,result))
print(x)
p =[x for x in num if x%2==0]
print(p)

