INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def visible(x, y, trees):
  if x == 0 or y == 0 or x == len(trees)-1 or y == len(trees[0])-1:
    return True
  if (int(trees[x][y]) > max([int(trees[x][i]) for i in range(y)]) or
      int(trees[x][y]) > max([int(trees[x][i]) for i in range(y+1, len(trees[0]))]) or
      int(trees[x][y]) > max([int(trees[i][y]) for i in range(x)]) or
      int(trees[x][y]) > max([int(trees[i][y]) for i in range(x+1, len(trees))])):
      return True
  return False   

def calc_score(x, y, trees):
  if x == 0 or y == 0 or x == len(trees)-1 or y == len(trees[0])-1:
    return 0
  A = [0] * 4
  A[0] = [int(trees[x][i]) for i in range(y)]; A[0] = A[0][::-1] # left
  A[1] = [int(trees[x][i]) for i in range(y+1, len(trees[0]))] # right 
  A[2] = [int(trees[i][y]) for i in range(x)]; A[2] = A[2][::-1] # up
  A[3] = [int(trees[i][y]) for i in range(x+1, len(trees))] # down
 
  B = [1] * 4
  c = 1
  for d in range(4): 
    for i, val in enumerate(A[d]):
      if val >= int(trees[x][y]) or i == len(A[d])-1:
        break
      B[d] += 1
    c *= B[d]
  return c

def main():
  trees = extract_input(INPUT)

  res = 0
  for x in range(len(trees)):
    for y in range(len(trees[0])):
      res = max(res, calc_score(x, y, trees))
      pass
  print(res)

if __name__ == '__main__':
  main()
