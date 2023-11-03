nome = input()
sal = float(input())
vendas = float(input())
comis = (vendas*15)/100
total = sal + comis
print(f'TOTAL = R$ {total:.2f}')