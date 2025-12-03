
with open("asdf") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val == '#': print(i, j)
