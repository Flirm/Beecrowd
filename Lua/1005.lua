a = io.read()
b = io.read()
media = (a*3.5 + b*7.5)/11
media = string.format("%.5f", media)
print("MEDIA = "..media)