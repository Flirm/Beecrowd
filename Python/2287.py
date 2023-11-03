testes = 0
senhas = []
n = int(input())
while n != 0:
    testes += 1
    associacao = []
    digitos = []
    for i in range(n):
        holder = input().split()
        associacao.append(holder[:10])
        digitos.append(holder[10:])
    x = []
    for i in range(6):
        s = []
        rep = []
        for j in range(n):
            dig = digitos[j][i]
            if dig == 'A':
                s.append(associacao[j][:2])
            elif dig == 'B':
                s.append(associacao[j][2:4])
            elif dig == 'C':
                s.append(associacao[j][4:6])
            elif dig == 'D':
                s.append(associacao[j][6:8])
            elif dig == 'E':
                s.append(associacao[j][8:])
        for k in range(n):
            for l in range(2):
                rep.append(s[k][l])
        repetidos = [x for x in rep if rep.count(x) > (n-1)]
        x.append(repetidos[0])
    x = ' '.join(x)
    senhas.append(x)
    n = int(input())
    
for i in range(testes):
    print(f'Teste {i+1}')
    print(senhas[i], end = ' \n')
    print()