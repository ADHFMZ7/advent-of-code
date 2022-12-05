INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

class cargo:
  def __init__(self, lines):
    
    setup, commands = lines[:8], lines[10:]
    print(commands)
    self.stacks = self.create_stacks(9, setup)
    self.print_cargo() 

    for command in commands:
      self.move_box(command)

  def print_cargo(self):
    for i in range(len(self.stacks)):
      print(i+1, self.stacks[i])
    print('\n')

  def create_stacks(self, num, lines):
    stacks = []
    for i in range(num):
      stacks.append([])
    for line in lines[:8]:
      i = 0 
      for char in line[1::4]:
        if char != ' ':
          stacks[i].append(char)
        i = i + 1 if i < 9 else 0
    for i in range(9):
      stacks[i] = stacks[i][::-1]
    return stacks 

  def move_box(self, line):
    qty, src, dst = map(int, line.split()[1::2])
    src, dst = src-1, dst-1
    crane = [] 
    for i in range(qty):
      crane.append(self.stacks[src].pop())
    self.stacks[dst] += crane[::-1]
    self.print_cargo()

  def extract_answer(self):
    ans = ''
    for crate in self.stacks:
      ans += crate.pop()
    return ans

def main():
  lines = extract_input(INPUT)
  thing = cargo(lines)
  print(f"The answer is {thing.extract_answer()}")

if __name__ == '__main__':
  main()
