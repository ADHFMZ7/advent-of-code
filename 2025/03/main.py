import sys
from functools import reduce

def parse_input(filename: str):
    
    with open(filename) as f:
        lines = f.readlines()

    return [[int(char) for char in bank[:-1]] for bank in lines]

def max_joltage(line) -> int:
    res, m = 0, 0

    for r in line:
        res = max(res, 10*m + r)
        m = max(m, r)
    return res

def max_joltage_2(line: list[int]) -> int:
    r = 11
    res = 0

    while r >= 0:
        val = max(line[:-r] if r else line)
        line = line[line.index(val)+1:]
        res += val * (10**r)

        r -= 1

    return res

def part1(banks):
    return reduce(lambda a,b: a+b, map(max_joltage, banks))

def part2(banks):
    return reduce(lambda a,b: a+b, map(max_joltage_2, banks))

def main():

    if len(sys.argv) != 2:
        exit(1)

    data = parse_input(sys.argv[1])

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")

if __name__ == '__main__':
    main()
