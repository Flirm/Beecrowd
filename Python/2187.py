n = int(input())
cases = []
while n != 0:
    i, j, k, l = 0, 0, 0, 0
    while n >= 50:
        i += 1
        n -= 50
    while n >= 10:
        j += 1
        n -= 10
    while n >= 5:
        k += 1
        n -= 5
    while n >= 1:
        l += 1
        n -= 1
    cases.append(f'{i} {j} {k} {l}')
    n = int(input())
for i in range(len(cases)):
    print(f'Teste {i+1}')
    print(cases[i])
    print()