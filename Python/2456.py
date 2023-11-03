c = list(map(int, input().split()))
normal = True
cres = 0
desc = 0
for i in range(len(c)-1):
    if c[i+1] < c[i]:
        desc += 1
        normal = False
    else:
        cres += 1
        normal = True
if cres != 0 and desc != 0:
    print('N')
elif normal == True:
    print('C')
else:
    print('D')
        