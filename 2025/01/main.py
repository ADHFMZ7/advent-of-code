


with open('input.txt') as f:
    lines = f.readlines()

rots = [(x[0], int(x[1:])) for x in lines]

pos = 50

counter = 0

for dir, dpos in rots:

    if dir == 'L':
        pos = (pos - dpos) % 100
    else:
        pos = (pos + dpos) % 100
    
    if pos == 0:
        counter += 1

print(counter)

pos = 50
counter = 0

for dir, dpos in rots:

    sign = -1 if dir == 'L' else 1

    for _ in range(0, abs(dpos)):

        pos = (pos + sign) % 100
    
        if pos == 0:
            counter += 1

print(counter)
