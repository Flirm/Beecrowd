n = int(input())
fat = 1
while n-1 > 0:
    fat = fat * n
    n -= 1
print(fat)