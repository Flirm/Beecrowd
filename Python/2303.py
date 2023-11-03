l, c, m, n = map(int, input().split())
#getting garden matrix
plantacao = []
for i in range(l):
    try:
        linha = list(map(int, input().split()))
    except:
        break
    plantacao.append(linha)

major = 0
jumperM = 0
for k in range(l//m):
    jumperN = 0
    for s in range(c//n):
        lote = 0
        for i in range(m):
            for j in range(n):
                lote += plantacao[i+jumperM][j+jumperN]
        if lote > major:
            major = lote
        jumperN += n
    jumperM += m
    
print(major)