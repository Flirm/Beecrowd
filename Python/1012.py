A, B, C = map(float, input().split())
atri = (A*C)/2
acirc = 3.14159*C**2
atrap = ((A+B)/2)*C
aqua = B**2
aret = A*B
print(f'TRIANGULO: {atri:.3f}\nCIRCULO: {acirc:.3f}\nTRAPEZIO: {atrap:.3f}\nQUADRADO: {aqua:.3f}\nRETANGULO: {aret:.3f}')