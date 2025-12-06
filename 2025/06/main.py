import sys
from functools import reduce

func = {'+': lambda a, b: a + b, '*': lambda a, b: a * b}

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    ops = [func[op] for op in lines[-1].split()]
    return lines[:-1], ops

def p1(lines, ops):

    nums = zip(*[map(int, line.split()) for line in lines])
    return sum(reduce(op, num) for op, num in zip(ops, nums))

def p2(lines, ops):
    nums = [[0]]

    for col in range(len(lines[0])):
        base = 1
        c = 0
        for row in reversed(range(len(lines))):
            if lines[row][col].isalnum():
                nums[-1][-1] += base * int(lines[row][col])
                base *= 10
            else:
                c += 1
        if c == len(lines):
            nums[-1].pop()
            nums.append([])
        nums[-1].append(0)
    return sum(reduce(op, num) for num, op in zip(nums, ops))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit(1)

    nums, ops = parse_input(sys.argv[1])

    print(f"Answer to part 1: {p1(nums, ops)}")
    print(f"Answer to part 2: {p2(nums, ops)}")
