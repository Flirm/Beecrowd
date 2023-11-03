t = int(input())
competidores = list(map(int, input().split()))
n = 0
for i in competidores:
    if(i == t):
        n += 1
print(n)