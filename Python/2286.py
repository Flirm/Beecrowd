N = 1
partida = []
num = 0
while N != 0:
    num += 1
    N = int(input())
    if(N == 0):
        break
    nome1 = input()
    nome2 = input()
    partida.append(f'Teste {num}')
    for i in range(N):
        jogo = list(map(int, input().split()))
        if(jogo[0]+jogo[1])%2:
            partida.append(nome2)
        else:
            partida.append(nome1)
    partida.append('')

for i in partida:
    print(i)