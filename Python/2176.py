n = input()
bitCount = 0
for i in n:
    if i == '1':
        bitCount += 1
if bitCount%2 == 0:
    print(n+'0')
else:
    print(n+'1')