n = int(input())
dentro = 0
out = 0
for i in range(n):
    x = int(input())
    if x > 9 and x < 21:
        dentro += 1
    else:
        out += 1
print(f'{dentro} in')
print(f'{out} out')