dias = int(input())
meses = 0
anos = 0
while(dias >= 365):
    dias -= 365
    anos += 1
while(dias >= 30):
    dias -= 30
    meses += 1
print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')