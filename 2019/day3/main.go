package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("input")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var wire1 []string
	var wire2 []string
	for scanner.Scan() {
		line := scanner.Text()
		wire1, wire2 = parseInput(line)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	fmt.Printf("Part 1: %d\n", part1(wire1))
	fmt.Printf("Part 2: %d\n", part2(wire2))
}

type vec2 struct {
	x int
	y int
}

func part1(wire []string) int {

	fmt.Println(wire)
	return 0
}

func part2(wire []string) int {

	return 0

}

func parseInput(line string) ([]string, []string) {

	strValues := strings.Split(line, "\n")


	var wire1 []string
	wire1 = strings.Split(strValues[0], ",")


	var wire2 []string
	wire2 = strings.Split(strValues[1], ",")

	return wire1, wire2
}

