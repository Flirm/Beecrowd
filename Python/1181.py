l = int(input())
resp = input()
M = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)

soma = 0
for i in M[l]:
    soma += i
if resp == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/12:.1f}')