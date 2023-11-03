def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        c = 0
        while(n-1):
            c=a+b
            a=b
            b=c
            n=n-1
        return c
        
numeros = []
respostas = []
t = int(input())
for i in range(t):
    num = int(input())
    resp = fibo(num)
    numeros.append(num)
    respostas.append(resp)

for i in range(len(numeros)):
    print(f'Fib({numeros[i]}) = {respostas[i]}')