

def valid1(code):
    s = str(code)

    if len(s) % 2:
        return True

    return int(s[:len(s) // 2]) != int(s[len(s)//2:])


def valid2(code):
    s = str(code)

    for win in range(1, len(s)):
        block = set(s[start:start+win] for start in range(0, len(s), win))
        if len(block) == 1:
            return False
    return True

with open('input.txt') as f:
    ranges = [tuple(map(int, x.split('-'))) for x in f.read().split(',')]

res = 0

for ix, (l, r) in enumerate(ranges):
    print(ix/len(ranges))
    for code in range(l, r+1):
        if not valid2(code):
            res += code

print(res)
