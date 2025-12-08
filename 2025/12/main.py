import sys


def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    return # processed lines


def p1(data):
    ...

def p2(data):
    ...

if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit(1)

    data = parse_input(sys.argv[1])

    print(f"Answer to part 1: {p1(data)}")
    print(f"Answer to part 2: {p2(data)}")
