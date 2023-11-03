precos = [4, 4.5, 5, 2, 1.5]
pedido, quantidade = map(int, input().split())
valor = precos[pedido-1]*quantidade
print(f'Total: R$ {valor:.2f}')