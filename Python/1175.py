n = []
for i in range(20):
    n.append(input())
for i in range(10):
    n[i], n[-(i+1)] = n[-(i+1)], n[i]
for i in range(20):
    print(f'N[{i}] = {n[i]}')