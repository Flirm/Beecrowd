local n = io.read("n")

for i = 1, n do
    local num = io.read("n")
    if num == 0 then
        print("NULL")
    else
        local oddity = (num&1 == 1) and "ODD" or "EVEN"
        local positive = (num > 0) and "POSITIVE" or "NEGATIVE"
        print(oddity.." "..positive)
    end
end