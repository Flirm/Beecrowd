t = int(input())
resp = []
morse = {'=.===':'a', '===.=.=.=':'b', '===.=.===.=':'c', '===.=.=':'d', '=':'e', '=.=.===.=':'f', '===.===.=':'g', '=.=.=.=':'h', '=.=':'i', '=.===.===.===':'j', '===.=.===':'k', '=.===.=.=':'l', '===.===':'m', '===.=':'n', '===.===.===':'o', '=.===.===.=':'p', '===.===.=.===':'q', '=.===.=':'r', '=.=.=':'s', '===':'t', '=.=.===':'u', '=.=.=.===':'v', '=.===.===':'w', '===.=.=.===':'x', '===.=.===.===':'y', '===.===.=.=':'z'}
for i in range(t):
    s = ''
    cod = input().split('.......')
    for i in cod:
        letras = i.split('...')
        for j in letras:
            s = s + morse[j]
        if i != cod[-1]:
            s = s + ' '
    resp.append(s)
for i in resp:
    print(i)