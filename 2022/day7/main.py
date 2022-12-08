INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return list(file.read().splitlines())

class directory:

  def __init__(self, name='/', prev=None):
    self.name = name
    self.subdirs = []
    self.size = 0
    self.prev = prev 
    
  def ls(self, index, lines):
    index += 1
    while index != len(lines) and lines[index][0] != '$':
      arg1, arg2 = lines[index].split()
      if arg1 == 'dir':
        self.add_directory(arg2)
        #print(f"added directory {arg2}")
      else:
        self.size += int(arg1)
        #print(f"added file {arg2} of size {arg1}")
      index += 1

  def compute_size(self):
    if not self.subdirs:
      return self.size
    res = 0
    for i in self.subdirs:
      temp = i.compute_size()
      res += temp
    self.size += res
    return self.size

  def add_directory(self, name):
    temp = directory(name, self)
    self.subdirs.append(temp) 

  def cd(self, new):
    if new == '..':
      return self.prev
    for i in self.subdirs:
      if i.name == new:
        return i

def final_score(root):
  root.compute_size()
  curr = root
  counter = 0
  while curr:
    if curr.size <= 


def main():
  lines = extract_input(INPUT)

  root = directory('_')
  root.add_directory('/')
  curr = root
  
  for i, line in enumerate(lines[:50]):
    #print(line)
    if line[0] == "$":
      if 'ls' in line:
        curr.ls(i, lines)
      elif 'cd' in line:
        curr = curr.cd(line.split()[2])
  root.compute_size()


  def dfs(root):
    print(root.name, ': ', root.size)
    res = 0
    for i in root.subdirs:
      res += dfs(i)
    
  dfs(root)

  #print(f"Total size is {final_score(root)}")

if __name__ == '__main__':
  main()
