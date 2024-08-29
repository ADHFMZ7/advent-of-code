with open("input") as file:

    wire1 = file.readline().split(',')
    wire2 = file.readline().split(',')


def create_set(wire):

    ret = set()
    vec = [0, 0]

    for cmd in wire:
        
        direction = cmd[0]
        magnitude = cmd[1:]
        cumdist = 0 


        if direction == "U":
            dx = [0, 1]
        elif direction == "D":
            dx = [0, -1]
        elif direction == "L":
            dx = [-1, 0]
        elif direction == "R":
            dx = [1, 0]
        else:
            dx = (0, 0)


        for i in range(int(magnitude)):
            cumdist += 1
            vec[0] += dx[0]
            vec[1] += dx[1]
            ret.add(tuple([vec, cumdist]))

    return ret   

w1 = create_set(wire1)
w2 = create_set(wire2)

m_dist = lambda x : abs(x[0]) + abs(x[1])

# print(m_dist(sorted(w1 & w2, key=m_dist)[0]))

print(w1 & w2)
