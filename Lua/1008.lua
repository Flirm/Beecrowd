num = io.read()
hours = io.read()
pay = io.read()
print("NUMBER = "..num.. "\n" ..
      "SALARY = U$ "..(string.format("%.2f", hours*pay)))