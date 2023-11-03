n = int(input())
resp = []
for i in range(n):
    frase = input()
    primeiro = True
    palavra = ''
    for letra in frase:
        if letra != ' ' and primeiro == True:
            palavra = palavra + letra
            primeiro = False
        elif letra == ' ':
            primeiro = True
    resp.append(palavra)
for i in resp:
    print(i)