n = int(input())
texto = []
for i in range(n):
    lista = input()
    s = list(lista.split())
    s = sorted(s, reverse=True, key=lambda word: len(word))
    texto.append(' '.join(s))
for i in texto:
    print(i)