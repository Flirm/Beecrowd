n = int(input())
par = []
impar = []
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort(reverse = True)
for i in par:
    print(i)
for i in impar:
    print(i)