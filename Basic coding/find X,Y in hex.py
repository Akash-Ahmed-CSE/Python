print("Enter Octal Number: ", end="")
octal = input()

dnum = int(octal, 8)
hnum = hex(dnum)
n = str(hnum)
print("\nEquivalent Hexadecimal Value =", n[2:])

f=n[2:]
print("X is :",f[2])
print("y is :",f[3])