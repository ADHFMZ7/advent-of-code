import itertools

INPUT = 'input'

file = open(INPUT, 'r')
lines = list(file.read().splitlines())

R = len(lines)
C = len(lines[0])
target = "XMAS"

a = [-1, 0, 1]

directions = itertools.product(a, a)


res1 = 0
res2 = 0
     
for r, row in enumerate(lines):
  for c, char in enumerate(row):

    if char == 'A':

      count = 0
      dirs = [(-1, -1), (-1, 1)]
      for dr, dc in dirs:
        try: temp = lines[r+dr][c+dc] + lines[r-dr][c-dc]
        except: break
        if 'M' in temp and 'S' in temp:
          count += 1
      if count == 2:
        res2 += 1


    if char == 'X':
      for dr, dc in itertools.product(a, a):
        count = 0
        for i in range(4):
          if (0 <= r + i * dr < R) and (0 <= c + i * dc < C) and lines[r + i * dr][c + i * dc] == target[i]:
            count += 1
            continue
          break 
        if count == 4:
          res1 += 1

print(res1, res2) 













  


