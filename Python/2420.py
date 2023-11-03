n = int(input())
a = list(map(int, input().split()))
var = 0
t = None
sumA = a[0]
sumB = 0
indexA = 1
indexB = 0
for i in range(n-1):
    if indexA + indexB == n:
        break
    if sumA > sumB:
        sumB += a[-(1+indexB)]
        indexB += 1
    elif sumB > sumA:
        sumA += a[indexA]
        indexA += 1
    else:
        sumA += a[indexA]
        sumB += a[-(1+indexB)]
        indexA += 1
        indexB += 1
print(indexA)