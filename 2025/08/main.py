import sys
from itertools import combinations
from dataclasses import dataclass
from functools import reduce

def parse_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    return [Vec3D(*map(int, line.split(','))) for line in lines]

class UnionFind:
    def __init__(self, items):
        self.parent = {item: item for item in items}
        self.size = {item: 1 for item in items}
        self.b1, self.b2 = Vec3D(0,0,0), Vec3D(0,0,0)

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)

        if root1 != root2:
            if self.size[root1] < self.size[root2]:
                root1, root2 = root2, root1 
            
            self.parent[root2] = root1
            self.size[root1] += self.size[root2]
            del self.size[root2]

            self.b1 = item1
            self.b2 = item2
            return True # Merged successfully
        return False # Already in the same set

    def last_connected(self):
        return self.b1.x * self.b2.x

@dataclass(frozen=True)
class Vec3D:
    x: int 
    y: int 
    z: int 

def dist(x):
    p1, p2 = x
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)**0.5

def p1(junctions):

    candidates = sorted(combinations(junctions, 2), key=dist, reverse=True)
    circuits = UnionFind(junctions)

    num_connections = 1000

    for i in range(num_connections):
        p1, p2 = candidates.pop()
        circuits.union(p1, p2)

    largest_three = sorted(circuits.size.values(), reverse=True)[:3]
    return reduce(lambda x, y: x*y, largest_three)

def p2(junctions):
    candidates = sorted(combinations(junctions, 2), key=dist, reverse=True)
    circuits = UnionFind(junctions)

    while len(circuits.size) > 1:
        p1, p2 = candidates.pop()
        circuits.union(p1, p2)
    
    return circuits.last_connected()

if __name__ == '__main__':

    if len(sys.argv) != 2:
        exit(1)

    data = parse_input(sys.argv[1])

    print(f"Answer to part 1: {p1(data)}")
    print(f"Answer to part 2: {p2(data)}")
