r = int(input())
vencedores = []
while r != 0:
    aCount = 0
    bCount = 0
    for i in range(r):
        a, b = map(int, input().split())
        aCount += a
        bCount += b
    if aCount > bCount:
        vencedores.append('Aldo')
    else:
        vencedores.append('Beto')
    r = int(input())

for i in range(len(vencedores)):
    print(f'Teste {i+1}')
    print(vencedores[i])
    print()