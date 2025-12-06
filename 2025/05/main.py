import sys
from collections import deque

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    ranges = [tuple(map(int, line.split('-'))) for line in lines if '-' in line]
    ids = [int(line.strip('\n')) for line in lines if line.strip('\n').isnumeric()]

    ranges = sorted(ranges) 

    return ranges, ids

def p1(ranges, ids):
    ret = 0

    for id in ids:
        for i1, i2 in ranges:
            if id in range(i1, i2+1):
                ret += 1
                break

    return ret

def p2(ranges):
    stack = ranges[:1]
    ranges = ranges[1:]

    for cur in ranges: 
        if not stack:
            stack.append(cur)
            continue
        
        if stack[-1][1] >= cur[0]:
            i1, i2 = stack.pop()
            stack.append((i1, max(cur[1], i2)))
        else:
            stack.append(cur)


    return sum(map(lambda x: x[1]-x[0] + 1, stack))

if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit(1)

    ranges, ids = parse_input(sys.argv[1])

    print(f"Answer to part 1: {p1(ranges, ids)}")
    print(f"Answer to part 2: {p2(ranges)}")

