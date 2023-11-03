lados = list(map(float, input().split()))
lados.sort(reverse = True)
if lados[0] >= (lados[1] + lados[2]):
    print('NAO FORMA TRIANGULO')
    exit()
if lados[0]**2 == (lados[1]**2 + lados[2]**2):
    print('TRIANGULO RETANGULO')
if lados[0]**2 > (lados[1]**2 + lados[2]**2):
    print('TRIANGULO OBTUSANGULO')
if lados[0]**2 < (lados[1]**2 + lados[2]**2):
    print('TRIANGULO ACUTANGULO')
if lados[0] == lados[1] and lados[1] == lados[2]:
    print('TRIANGULO EQUILATERO')
if (lados[0] == lados[1] and lados[0] != lados[2]) or (lados[1] == lados[2] and lados[1] != lados[0]) or (lados[0] == lados[2] and lados[0] != lados[1]):
    print('TRIANGULO ISOSCELES')