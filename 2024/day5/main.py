import itertools 
with open("input", encoding="utf-8") as file:
    rules = {}

    while (line := str(file.readline())) != "\n":
        a, b = map(int, line.strip().split('|'))
        rules[a] = rules.get(a, []) + [b]
    lines = list(map(lambda x: list(map(int, x.strip().split(','))), file.readlines()))

def valid(nums):
    seen = set()
    for num in nums:
        if num in rules.keys(): 
            for b in rules.get(num, []):
                if b in nums and b in seen:
                    return False
        seen.add(num)
    return True

s = 0
bs = []
for line in lines:
    if valid(line):
        s += line[len(line) // 2]
        continue
    bs.append(line)

t = 0
for nums in bs:
    for combo in itertools.permutations(nums):
        if valid(combo):
            t += combo[len(combo) // 2]
            break

# print(bs)
# for nums in bs:
#     seen = set()
#     for ix, num in enumerate(nums):
#         if num in rules.keys():
#             for b in rules.get(num, []):
#                 if b in nums and b not in seen:
#                     nums[ix], nums[nums.index(b)] = nums[nums.index(b)], nums[ix]
#                     if valid(nums):
#                         break
print(t)
