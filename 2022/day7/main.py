INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

class directory:

  def __init__(self, name='/', prev='/'):
    self.name = name
    self.subdirs = []
    self.size = 0
    self.prev = prev if prev != '/' else self
    
  def ls(self, index, lines):
    index += 1
    while index != len(lines) and lines[index][0] != '$':
      arg1, arg2 = lines[index].split()
      if arg1 == 'dir':
        print(f"Added directory {arg2}")
        self.add_directory(arg2)
      else:
        print(f"Added file of size {arg1} called {arg2}")
        self.size += int(arg1)
      index += 1

  def compute_size(self):
    if not self.subdirs:
      return self.size
    res = 0
    for i in self.subdirs:
      res += i.compute_size()
    self.size += res
    return self.size

  def add_directory(self, name):
    temp = directory(name, self) 
    self.subdirs.append(temp)
    return temp

  def cd(self, new):
    if new == '..':
      return self.prev
    for i in self.subdirs:
      if i.name == new:
        return i
    return self.add_directory(new)


def final_score(root):
  score = 0
  score += root.size if root.size <= 100000 else 0
  print(root.name, root.size)
  for i in root.subdirs:
    score += final_score(i)
  return score


def final_score2(root):
  target = root.size - 40000000
  def bfs(root):
    valid_dirs = []
    if root.size >= target:
      valid_dirs.append(root.size)
    for i in root.subdirs:
      valid_dirs += bfs(i)
    return valid_dirs
  return min(bfs(root))

def main():
  lines = extract_input(INPUT)

  root = directory('_')
  root.add_directory('/')
  curr = root
  
  for i, line in enumerate(lines):
    print(i, line)
    if line[0] == "$":
      if 'ls' in line:
        curr.ls(i, lines)
      elif 'cd' in line:
        curr = curr.cd(line.split()[2])
        print(f"  Changed into directory {curr.name}")
  root.compute_size()
  
  print(f"Total size is {final_score(root)}")
  print(f"The smallest file that will work is {final_score2(root)}")

if __name__ == '__main__':
  main()
