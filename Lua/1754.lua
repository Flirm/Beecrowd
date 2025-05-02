t = io.read("*n")

for i=t,1,-1
do
    x, y = io.read("*n", "*n")
    x = math.ceil(x/y)
    if x < 2 then
        x = 2
    end
    print(x)
end