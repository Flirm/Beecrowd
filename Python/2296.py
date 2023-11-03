import sys
N = int(input())
menor = sys.maxsize
num = None
for i in range(N):
    M, *trilha = map(int, input().split())
    diff_ida, diff_volta = 0, 0
    for altura in range(M-1):
        if(trilha[altura] > trilha[altura+1]):
            diff_ida += (trilha[altura] - trilha[altura+1])
        else:
            diff_volta += (trilha[altura+1] - trilha[altura])
    if diff_ida > diff_volta:
        esforco = diff_volta
    else:
        esforco = diff_ida
    if esforco < menor:
        menor = esforco
        num = i
print(num+1)