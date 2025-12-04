import sys


def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    
    return [[x for x in line[:-1]] for line in lines]

def p1(grid):

    rows, cols = len(grid), len(grid[0])
   
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    res = 0

    for x, row in enumerate(grid):
        for y, val in enumerate(row):
              
            if val != '@':
                continue

            rolls = 0

            for dx, dy in dirs:
                if x+dx in range(rows) and y+dy in range(cols):
                    if grid[x+dx][y+dy] == '@':
                        rolls += 1
            
            if rolls < 4:
                res += 1

    return res



def p2(grid):

    rows, cols = len(grid), len(grid[0])
   
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    res = 0
    q = [1] 
    while q:
        q = []
        for x, row in enumerate(grid):
            for y, val in enumerate(row):

                if val != '@':
                    continue

                rolls = 0

                for dx, dy in dirs:
                    if x+dx in range(rows) and y+dy in range(cols):
                        if grid[x+dx][y+dy] == '@':
                            rolls += 1

                if rolls < 4:
                    q.append((x, y))

        res += len(q)

        for x, y in q:
            grid[x][y] = '.'

    return res

if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit(1)

    data = parse_input(sys.argv[1])

    print(f"Answer to part 1: {p1(data)}")
    print(f"Answer to part 2: {p2(data)}")
