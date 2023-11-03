n = int(input())
resp = []
def enqueue(perm, origin):
    queued = list(reversed(origin[:origin.index(perm[0])+1]))
    for i in range(len(queued)):
        if perm[0] not in queued:
            return enqueue(perm, origin)
        elif queued[0] != perm[0]:
            return False
        del origin[origin.index(perm[0])], queued[0], perm[0]
    return True
while n != 0:
    while True:
        perm = list(map(int, input().split()))
        if perm[0] == 0:
            resp.append("")
            break
        origin = [n for n in range(1, n+1)]
        possible = True
        while possible:
            possible = enqueue(perm, origin)
            if not perm:
                resp.append("Yes")
                break
            elif not possible:
                resp.append("No")

            
    n = int(input())
for i in resp:
    print(i)