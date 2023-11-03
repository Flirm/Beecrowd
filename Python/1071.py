x = int(input())
y = int(input())
soma = 0
if x > y:
    menor = y+1
    maior = x
else:
    menor = x+1
    maior = y
while(menor < maior):
    if menor % 2 != 0:
        soma += menor
    menor += 1
print(soma)