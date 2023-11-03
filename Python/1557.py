import math
t = int(input())
listaDeMatrizes = []
while t != 0:
    n = 1
    p = 1
    matriz = []
    for i in range(t):
        linha = []
        for j in range(t):
            linha.append(n * p)
            p = p * 2
        matriz.append(linha)
        n = n * 2
        p = 1
    listaDeMatrizes.append(matriz)
    t = int(input())

for matriz in listaDeMatrizes:
    digits = int(math.log(matriz[-1][-1],10))
    for linha in matriz:
        for elemento in linha:
            digE = int(math.log(elemento,10))
            print(' '*(digits-digE),end='')
            print(elemento, end = '')
            if elemento != linha[-1]:
                print(end=' ')
        print()
    print()