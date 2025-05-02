num = tonumber(io.read())

total = 0

if num <= 2000
then 
  print("Isento")
else
  if num > 3000
  then 
    if num > 4500
    then
      total = total + (num-4500)*0.28
      num = num - (num - 4500)
    end
    total = total + (num-3000)*0.18
    num = num - (num - 3000)
  end
  total = total + (num-2000)*0.08
  print("R$ "..string.format("%.2f",total))
end