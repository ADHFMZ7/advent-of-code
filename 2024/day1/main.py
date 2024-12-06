

s = 0
l1 = []
c1 = {} 
l2 = []
c2 = {}
with open("input") as file:

    
    for line in file.readlines():
        line = line.split()
        l1.append(int(line[0]))
        l2.append(int(line[1]))
        c2[l2[-1]] = c2.get(l2[-1], 0) + 1
        # c2[l2[-1]] += 1

l1 = sorted(l1)
l2 = sorted(l2)

# for s1, s2 in zip(l1, l2):
for s1 in l1:
    s += s1 * c2[s1] if s1 in c2 else 0

print(s)
