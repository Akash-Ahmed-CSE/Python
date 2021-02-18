counts=dict()
print("Enter a lone for text :")
line=input("")
words=line.split()
print("words: ",words)
print("Continue...")
for word in words:
    counts[word] = counts.get(word,0)+1

print('Counts',counts)

for key in counts:
    print(key,counts[key])
#convert the dictonary to list
jjj=counts
print(list(jjj))
#2nd way to convert
print(jjj.keys())
print(jjj.values())
print(jjj.items())
#tow iteration variables!
print("next.....................")

for key,value in jjj.items():
    print(key,value)

stuff = dict()
print(stuff.get('candy',-1))

