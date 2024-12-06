
def safe(nums):

    sign = 1 if nums[0] < line[1] else -1

    c = 0
    for ix, (c1, c2) in enumerate(zip(line, line[1:])):



        diff = int(c2) - int(c1) # negative if decreasing 

        if sign == 1 and diff in range(1, 4):
            c += 1
            continue
        elif sign == -1 and diff in range(-1, -4, -1):
            c += 1
            continue
        if ix + 2 >= len(line):
            continue
        diff1 = (int(line[ix+2]) - int(c1))
        diff2 = (int(line[ix+2]) - int(c2))
        if sign == 1 and diff1 in range(1, 4) or sign == 1 and diff2 in range(1, 4):
            c += 1
        elif sign == -1 and diff1 in range(-1, -4, -1) or sign == -1 and diff2 in range(-1, -4, -1):
            c += 1
    


    return 0
    


s = 0

with open("inputtest") as file:
    
    for line in file.readlines():
        nums = map(int, line.split())
        s += safe(nums)


        if c >= len(line) - 1:
            print(line)
            s += 1
print(s)
