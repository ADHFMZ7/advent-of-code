package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func mod(a, b int) int {
	return (a%b + b) % b
}

func part1(rots []int) int {

	counter := 0
	dial := 50

	for _, value := range rots {
		dial = mod((dial + value), 100)
		if dial == 0 {
			counter += 1
		}
	}

	return counter
}

func part2(rots []int) int {

	counter := 0
	dial := 50

	for _, value := range rots {
		if value < 0 {
			for ix := 0; ix > value; ix-- {
				dial = mod(dial-1, 100)
				if dial == 0 {
					counter += 1
				}
			}
		} else {
			for ix := 0; ix < value; ix++ {
				dial = mod(dial+1, 100)
				if dial == 0 {
					counter += 1
				}
			}
		}

	}

	return counter
}

func main() {

	file, err := os.Open("input.txt")
	if err != nil {
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	s := make([]int, 0)

	for scanner.Scan() {
		line := scanner.Text()

		num, err := strconv.Atoi(line[1:])
		if err != nil {
			return
		}
		if line[0] == 'L' {
			num *= -1
		}
		s = append(s, num)
	}

	fmt.Printf("Answer to part 1: %d\n", part1(s))
	fmt.Printf("Answer to part 2: %d\n", part2(s))

}
