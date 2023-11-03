n = int(input())
resp = []
for i in range(n):
    text = list(input())
    tamanho = len(text)
    for char in range(tamanho):
        if text[char].isalpha():
            text[char] = chr(ord(text[char])+3)
    for char in range(tamanho//2):
        temp = text[char]
        text[char] = text[-(char+1)]
        text[-(char+1)] = temp
    for char in range(tamanho//2, tamanho):
        text[char] = chr(ord(text[char])-1)
    resp.append("".join(text))
for i in resp:
    print(i)