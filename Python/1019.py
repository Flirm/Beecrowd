seg = int(input())
minut = 0
hora = 0
while(seg >= 60):
    seg -= 60
    minut += 1
while(minut >= 60):
    minut -= 60
    hora += 1
print(f'{hora}:{minut}:{seg}')