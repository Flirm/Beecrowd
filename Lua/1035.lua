a = io.read()
t = {}

for str in string.gmatch(a, "([^%s]+)") do
  table.insert(t, tonumber(str))
end

if (t[2] > t[3]) and (t[4] > t[1]) and (t[3]+t[4] > t[1]+t[2]) and (t[1] & 1) == 0 and (t[3] >= 0) and (t[4] >= 0)
then
  print("Valores aceitos")
else
  print("Valores nao aceitos")