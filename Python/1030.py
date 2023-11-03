n = int(input())
resp = []
for i in range(n):
    n, k = map(int, input().split())
    sobreviventes = [1]*n
    for i in range(len(sobreviventes)):
        sobreviventes[i] = i+1
    index = 0
    while len(sobreviventes) != 1:
        index += k - 1
        while index >= len(sobreviventes):
            index -= len(sobreviventes)
        del sobreviventes[index]
    resp.append(sobreviventes[0])
for i in range(len(resp)):
    print(f"Case {i+1}: {resp[i]}")