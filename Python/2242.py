vogais = ['a','e','i','o','u']
a = input()
n = []
for i in range(len(a)):
    if a[i] in vogais:
        n.append(a[i])
engracado = True
for i in range(len(n)//2):
    if n[i] != n[-(i+1)]:
        engracado = False
if engracado == True:
    print('S')
else:
    print('N')