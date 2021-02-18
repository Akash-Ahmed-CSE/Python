s = input()
for word in s.split():
    s = s.replace(word, word.capitalize())
print(s)