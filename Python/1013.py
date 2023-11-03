a, b, c = map(int, input().split())
print(f'{max(a,b,c)} eh o maior')

#or#

a, b, c = map(int, input().split())
maior = (a+b+abs(a-b))//2
maior = (maior+c+abs(maior-c))//2
print(f'{maior} eh o maior')