local tab = {0, 1}

local n = io.read("n")

local function fib(num)
    if tab[num] ~= nil then
        return tab[num]
    end

    tab[num] = fib(num-1) + fib(num-2)
    return tab[num]
end
    
fib(n)
for index, value in ipairs(tab) do
    if index == n then
        print(value)
    else
        io.write(value.." ")
    end
end