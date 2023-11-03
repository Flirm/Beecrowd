horarios = []
while(True):
    try:
        h, m = map(int, input().split())
    except:
        break
    horas = h//30
    minutos = m//6
    if minutos >= 60:
        minutos -= 60
        horas += 1
    if horas >= 24:
        horas -= 24
    horario = f'{horas:02d}:{minutos:02d}'
    horarios.append(horario)
for i in horarios:
    print(i)