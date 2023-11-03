n = int(input())
resp = []
while n != 0:
    regions = [i+1 for i in range(n)]
    found = False
    m = 0
    while not found:
        index = 0
        m += 1
        tempReg = regions[:]
        while len(tempReg) > 1:
            del tempReg[index]
            index += m-1
            if 13 not in tempReg:
                break
            while index >= len(tempReg):
                index -= len(tempReg)
        if tempReg[0] == 13:
            found = True
        
    resp.append(m)
    n = int(input())
for i in resp:
    print(i)