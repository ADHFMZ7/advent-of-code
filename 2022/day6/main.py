INPUT = 'input'

def extract_input(filename):
  file = open(filename, 'r')
  return file.read()

def find_marker(line, bufsize):
  for i in range(bufsize, len(line)):
    if len(set(line[i-bufsize: i])) >= bufsize:
      return i


def main():
  line = extract_input(INPUT)
  print("first answer:", find_marker(line, 4))
  print("second answer:", find_marker(line, 14))

if __name__ == '__main__':
  main()
