n = int(input())
lista = []
for i in range(n):
    lista.append(input())
atual = ''
contador = 0
for i in lista:
    if i != atual:
        atual = i
        contador += 1
print(contador)