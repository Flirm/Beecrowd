n = int(input())
precos = []
for i in range(n):
    p, g = map(float, input().split())
    pF = (p/g)*1000
    precos.append(pF)
print(f'{min(precos):.2f}')