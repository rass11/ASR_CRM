def t2():
    with open('1.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
t2()

