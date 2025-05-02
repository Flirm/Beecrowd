temp = io.read()
vel = io.read()

litro = (temp*vel)/12

print(string.format("%.3f", litro))