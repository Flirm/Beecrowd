input()
r = list(map(int, input().split()))
reducao = False
for i in range(len(r)-1):
    if r[i] > r[i+1]:
        reducao = True
        print(i+2)
        break
if reducao == False:
    print(0)