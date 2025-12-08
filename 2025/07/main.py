import sys
from collections import deque


def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [list(line) for line in lines[:-1]]

class Split:
    def __init__(self, num):
        self.num = num
    def __repr__(self):
        return str(self.num)
    def __add__(self, other):
        return other + self.num
    def __radd__(self, other):
        return other + self.num

def p1(grid):
    beams = deque()
    for ix, val in enumerate(grid[0]):
        if val == 'S':
            beams.append(ix)
  
    ret = 0

    for ix, line in enumerate(grid[1:]):
        for _ in range(len(beams)):
            beam = beams.popleft()
            if line[beam] == '^':
                ret += 1
                if beam - 1 in range(len(grid[0])) and beam - 1 not in beams:
                    beams.append(beam - 1)

                if beam + 1 in range(len(grid[0])) and beam + 1 not in beams:
                    beams.append(beam + 1)
            else:
                beams.append(beam)
    return ret

def p2(grid):
  
    buf = [1 if val == 'S' else 0 for val in grid[0]]
    
    ret = 0
    
    for r, line in enumerate(grid):
        if r == 0:
            continue
        for c, val in enumerate(line):
            if grid[r][c] == '^':
                buf[c] = Split(buf[c]) if buf[c] else 0
            if isinstance(buf[c], Split):
                if c - 1 in range(len(buf)):
                    buf[c-1] += buf[c].num
                if c + 1 in range(len(buf)):
                    buf[c+1] += buf[c].num
                buf[c] = 0
            
    return sum(buf)


if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit(1)

    data = parse_input(sys.argv[1])

    print(f"Answer to part 1: {p1(data)}")
    print(f"Answer to part 2: {p2(data)}")
