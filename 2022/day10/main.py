INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().split())




class CPU:
  
  def __init__(self):
    self.x = 1
    self.cycle = 0
    self.vals = []
 
  def execute(self, op):
    self.cycle += 1
    if self.cycle in [20, 60, 100, 140, 180, 220]:
      self.vals.append(self.x * self.cycle)
    if op in ['noop', 'addx']:
      return 
    self.x += int(op)

  def signal_strengths(self):
    return sum(self.vals)

  def draw(self, lines):
    self.reset()

    for line in lines:
      if (self.cycle%40) in range(self.x-1, self.x+2):
        print('#', end='')  
        pass
      else:
        print(' ', end='')
        pass
      if (self.cycle % 40)+1 == 40:
        print('|\n|', end='')
        pass

      self.execute(line)

  def reset(self):
    self.x = 1
    self.cycles = 0


def main():
  lines = extract_input(INPUT)

  cpu = CPU()

  for line in lines:
    cpu.execute(line)

  print(f"The sum of the six signal strengths is: {cpu.signal_strengths()}\n")

  print("The following is the output of the CRT display:")
  print("|"+"="*40, end='|\n|')

  cpu.draw(lines)

  print("="*40, end = '|\n')

if __name__ == '__main__':
  main()


