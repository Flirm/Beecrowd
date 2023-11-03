respostas = []
dura = {'W':1, 'H':0.5, 'Q':0.25, 'E': 0.125, 'S':1/16, 'T':1/32, 'X':1/64}
n = list(input().split('/'))
while n[0] != '*':
    comp = 0
    for i in n:
        soma = 0
        for j in i:
            soma += dura[j]
        if soma == 1:
            comp += 1
    respostas.append(comp)
    n = list(input().split('/'))
for i in respostas:
    print(i)