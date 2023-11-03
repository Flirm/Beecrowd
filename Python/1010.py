p1 = list(map(float, input().split()))
p2 = list(map(float, input().split()))
val = p1[1]*p1[2] + p2[1]*p2[2]
print(f'VALOR A PAGAR: R$ {val:.2f}')