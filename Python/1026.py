resp = []
while True:
    try:
        nums = list(map(int, input().split()))
    except:
        break
    for i in range(len(nums)):
        nums[i] = bin(nums[i])[2:]
    new_num = ""
    diff = abs(len(nums[0]) - len(nums[1]))
    g = str(max(int(nums[0]), int(nums[1])))
    p = str(min(int(nums[0]), int(nums[1])))
    index = 0
    while diff != 0:
        new_num += g[index]
        index += 1
        diff -= 1
    for i in range(len(p)):
        if p[i] == g[index + i]:
            new_num += '0'
        else:
            new_num += '1'
    resp.append(int(new_num, 2))
for i in resp:
    print(i)