n = int(input())
numeros = []
nums_distintos = []
for i in range(n):
    num = int(input())
    numeros.append(num)
    if num not in nums_distintos:
        nums_distintos.append(num)

nums_distintos.sort()
for i in nums_distintos:
    a = numeros.count(i)
    print(f'{i} aparece {a} vez(es)')