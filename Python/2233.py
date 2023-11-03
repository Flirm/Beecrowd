r = int(input(), 16)
g = int(input(), 16)
b = int(input(), 16)
bCount = g//b
gCount = r//g
print(hex(1 + gCount**2 + bCount**2*gCount**2)[2:])