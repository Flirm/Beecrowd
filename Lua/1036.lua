a,b,c = io.read("*n","*n","*n")

delta = (b^2)-(4*a*c)

if a == 0 or delta < 0 then
    print("Impossivel calcular")
else
    r1 = (-b+math.sqrt(delta))/(2*a)
    r2 = (-b-math.sqrt(delta))/(2*a)
    print("R1 = "..string.format("%.5f", r1).."\n"
          .."R2 = "..string.format("%.5f", r2))
end
