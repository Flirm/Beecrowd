n, I, f = map(int, input().split())
v = list(map(int, input().split()))
sm = 0
for i in range(len(v)):
    for j in range(len(v)):
        if v[i] + v[j] >= I and  v[i] + v[j] <= f and i != j:
            sm += 1
print(int(sm/2))