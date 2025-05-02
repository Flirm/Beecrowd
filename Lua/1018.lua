n = io.read()
print(n)
cem = n // 100
n = n - cem*100
cinquenta = n // 50
n = n - cinquenta*50
vinte = n // 20
n = n - vinte*20
dez = n // 10
n = n - dez*10
cinq = n // 5
n = n - cinq*5
dois = n // 2
n = n - dois*2
print(cem.." nota(s) de R$ 100,00\n"..
      cinquenta.." nota(s) de R$ 50,00\n"..
      vinte.." nota(s) de R$ 20,00\n"..
      dez.." nota(s) de R$ 10,00\n"..
      cinq.." nota(s) de R$ 5,00\n"..
      dois.." nota(s) de R$ 2,00\n"..
      n.." nota(s) de R$ 1,00") 