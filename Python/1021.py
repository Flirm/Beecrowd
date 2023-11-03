n = float(input())
n = n*100
n100, n50, n20, n10, n5, n2, n1 = 0,0,0,0,0,0,0
m50, m25, m10, m5, m01 = 0,0,0,0,0
while n >= 10000:
    n100 += 1
    n -= 10000
while n >= 5000:
    n50 += 1
    n -= 5000
while n >= 2000:
    n20 += 1
    n -= 2000
while n >= 1000:
    n10 += 1
    n -= 1000
while n >= 500:
    n5 += 1
    n -= 500
while n >= 200:
    n2 += 1
    n -= 200
while n >= 100:
    n1 += 1
    n -= 100
while n >= 50:
    m50 += 1
    n -= 50
while n >= 25:
    m25 += 1
    n -= 25
while n >= 10:
    m10 += 1
    n -= 10
while n >= 5:
    m5 += 1
    n -= 5
while n >= 1:
    m01 += 1
    n -= 1
print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{n1} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m5} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')