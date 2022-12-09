INPUT = 'input'

offsets = {
  'R' : (0, 1),
  'L' : (0, -1),
  'U' : (1, 0),
  'D' : (-1, 0)
}


def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def touching(head, tail):
  if abs(head[0]-tail[0]) >= 2 or abs(head[1]-tail[1]) >= 2:
    return False
  return True

def move_knot(head, tail):
  if touching(head, tail):
    return
  for i in range(2):
    if head[i] == tail[i]:
      a = 1 if head[i] > tail[i] else -1
      tail[i] += 1

  if head[0] != tail[0] or head[1] != tail[1]:
    a = 1 if head[0] > tail[0] else -1
    b = 1 if head[1] > tail[1] else -1
    tail[0] += a; tail[1] += b
  return

def main():

  lines = extract_input(INPUT)
  knots = [[0, 0] for i in range(10)]
  tail_visit = set() 

  for line in lines:
    direction, amount = line.split()
    offset = offsets[direction]
    for i in range(int(amount)):
      tail_visit.add(tuple(knots[-1]))

      knots[0][0] += offset[0]; knots[0][1] += offset[1]
      for i in range(len(knots)-1):
        move_knot(knots[i], knots[i+1])
  print(len(tail_visit))

if __name__ == '__main__':
  main()
