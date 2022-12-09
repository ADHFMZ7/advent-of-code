INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

def touching(head, tail):
  if abs(head[0]-tail[0]) >= 2 or abs(head[1]-tail[1]) >= 2:
    return False
  return True

def main():

  lines = extract_input(INPUT)

  head, tail = [0, 0], [0, 0]
  tail_visit = set((0, 0)) 

  for line in lines:
    direction, amount = line.split()
    if direction == 'R':
      offset = (0, 1)
    elif direction == 'L':
      offset = (0, -1)
    elif direction == 'U':
      offset = (1, 0)
    elif direction == 'D':
      offset = (-1, 0)
    for i in range(int(amount)):

      head[0] += offset[0]; head[1] += offset[1]

      if head[0] == tail[0] and not touching(head, tail):
        a = 1 if head[1] > tail[1] else -1
        tail[1] += a
        tail_visit.add(tuple(tail))

      elif head[1] == tail[1] and not touching(head, tail):
        a = 1 if head[0] > tail[0] else -1
        tail[0] += a
        tail_visit.add(tuple(tail))

      elif not touching(head, tail) and (head[0] != tail[0] or head[1] != tail[1]):
        a = 1 if head[0] > tail[0] else -1
        b = 1 if head[1] > tail[1] else -1
        tail[0] += a; tail[1] += b
        tail_visit.add(tuple(tail))

  print(len(tail_visit))

if __name__ == '__main__':
  main()
