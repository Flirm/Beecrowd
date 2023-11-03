p = int(input())
soma = 0
menu = {1001:1.50, 1002:2.50, 1003:3.50, 1004:4.50, 1005:5.50}
for i in range(p):
    m, q = map(int, input().split())
    soma += menu[m] * q
print(f'{soma:.2f}')