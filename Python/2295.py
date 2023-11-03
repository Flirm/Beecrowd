a, g, ra, rg = map(float, input().split())
rend_a = ra/a
rend_b = rg/g
if rend_a > rend_b:
    print('A')
else:
    print('G')