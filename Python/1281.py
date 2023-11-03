n = int(input())
respostas = []
for q in range(n):
    mercado = {}
    m = int(input())
    for i in range(m):
        resp = list(input().split())
        nome = resp[0]
        preco = float(resp[1])
        mercado[nome] = preco
    p = int(input())
    valor = 0
    for i in range(p):
        resp = list(input().split())
        valor += mercado[resp[0]]*float(resp[1])
    respostas.append(valor)
for i in respostas:
    print(f'R$ {i:.2f}')