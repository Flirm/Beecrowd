dI, n = map(int, input().split())
jog = {'D':dI, 'E':dI, 'F':dI}
for i in range(n):
    op = input().split()
    j = op[1]
    if op[0] == 'C':
        jog[j] -= int(op[2])
    elif op[0] == 'V':
        jog[j] += int(op[2])
    else:
        j2 = op[2]
        jog[j] += int(op[3])
        jog[j2] -= int(op[3])
print(jog['D'], jog['E'], jog['F'])