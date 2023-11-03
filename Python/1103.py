h1, m1, h2, m2 = map(int, input().split())
resp = []
while True:
    if h1 == 0 and h2 == 0 and m1 == 0 and m2 == 0:
        break
    if h1 > h2:
        h2 += 24
    if h1 == h2 and m1 > m2:
        h2 += 24
    mAtual = m1 + h1*60
    mProg = m2 + h2*60
    tempo = mProg - mAtual
    resp.append(tempo)
    
    h1, m1, h2, m2 = map(int, input().split())
for i in resp:
    print(i)