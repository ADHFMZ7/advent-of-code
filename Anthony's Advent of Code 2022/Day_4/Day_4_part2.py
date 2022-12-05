INPUT = "Anthony's Advent of Code 2022/Day_4/input.txt"


def extract_input(filename):
    file = open(filename, 'r')
    return list(file.read().splitlines())


def function(list):
    index = 0

    for entries in list:

        entries = entries.replace("-", ' ')
        entries = entries.replace(",", ' ')
        arr1 = entries.split(" ")

        if ((int(arr1[1]) >= int(arr1[2]) and int(arr1[0]) <= int(arr1[3]))):
            index += 1
        else:
            pass

    print(index)


def main():
    lines = extract_input(INPUT)
    function(lines)


if __name__ == '__main__':
    main()
