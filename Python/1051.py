renda = float(input())
valor = 0
if renda <= 2000:
    print('Isento')
else:
    if renda - 4500 > 0:
        valor += (renda-4500)*(28/100)
        renda = renda - (renda-4500)
    if renda - 3000 > 0:
        valor += (renda-3000)*(18/100)
        renda = renda - (renda-3000)
    if renda - 2000 > 0:
        valor += (renda-2000)*(8/100)
    print(f'R$ {valor:.2f}')