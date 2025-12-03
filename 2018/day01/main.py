
from functools import reduce

with open("input", 'r') as file:
    nums = [x for x in file.read().splitlines()]
nums = list(map(int, nums))
print(reduce(lambda x, y: x + y, nums))

sum = 0
s = set()

ix = 0
while True:
    i = nums[ix]
    sum += i
    if sum in s and sum:
        print(s)
        break
    s.add(sum) 
    ix = (ix + 1) % len(nums)

print(sum)
