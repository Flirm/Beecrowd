num = int(input())
resp = []
for i in range(num):
    encaixa = True
    a, b = map(str, input().split())
    if len(b) > len(a):
        encaixa = False
    if encaixa == True:
        buffA = a[len(a)-len(b):]
        if buffA != b:
            encaixa = False
    if encaixa == True:
        resp.append('encaixa')
    else:
        resp.append('nao encaixa')
for i in resp:
    print(i)