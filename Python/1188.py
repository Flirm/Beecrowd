n = input()
M = []
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)
valores = []
f = 0
for i in range(7,12):
    for j in range(5-f, 7+f):
        valores.append(M[i][j])
    f += 1
    
    
soma = 0
for i in valores:
    soma += i
if n == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma/144:.1f}')