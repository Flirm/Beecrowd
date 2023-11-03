hi, mi, hf, mf = map(int, input().split())
if hi == hf and mi == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    mi = mi + hi*60
    mf = mf + hf*60
    if mf < mi:
        mf += 24*60
    diff = mf - mi
    horas = 0
    while(diff > 59):
        horas += 1
        diff -= 60
    print(f'O JOGO DUROU {horas} HORA(S) E {diff} MINUTO(S)')