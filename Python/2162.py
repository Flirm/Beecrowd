input()
h = list(map(int, input().split()))
pico = 0
vale = 0
if h[0] > h[1]:
    pico += 1
else:
    vale += 1
for i in range(len(h)-1):
    if h[i] > h[i+1]:
        vale += 1
    elif h[i] == h[i+1]:
        print(0)
        exit()
    else:
        pico += 1
if len(h)%2 == 0:
    if pico == vale:
        print(1)
    else:
        print(0)
else:
    if h[0] > h[1]:
        if pico == vale+1:
            print(1)
        else:
            print(0)
    else:
        if vale == pico + 1:
            print(1)
        else:
            print(0)
    