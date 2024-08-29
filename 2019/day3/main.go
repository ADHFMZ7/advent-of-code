package main

import (
	"fmt"
	"os"
	"strings"
	"io"
	"strconv"
)

func main() {

	f, err := os.Open("input")
	if err != nil {
	panic(err)
	}
	defer f.Close()
	b := new(strings.Builder)
	io.Copy(b, f)

	var wire1 []string
	var wire2 []string

	wire1, wire2 = parseInput(b.String())

	fmt.Printf("Part 1: %d\n", part1(wire1, wire2))
	fmt.Printf("Part 2: %d\n", part2(wire1, wire2))
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

type vec2 struct {
	x int
	y int
}

func part1(wire1, wire2 []string) int {

	s1 := make(map[vec2]bool)

	w1 := vec2{0, 0}

	for _, str := range wire1 {
		
		direction := str[0]
		magnitude, _ := strconv.Atoi(str[1:])

		var dx vec2

		if direction == 'R' {
			dx = vec2{1, 0}	
		} else if direction == 'L' {
			dx = vec2{-1, 0}	
		} else if direction == 'U' {
			dx = vec2{0, 1}	
		} else if direction == 'D' {
			dx = vec2{0, -1}	
		}

		for ix := 0; ix < magnitude; ix++ {
			w1.x += dx.x
			w1.y += dx.y
			s1[w1] = true
		}
	}

	w2 := vec2{0, 0}

	s2 := make(map[vec2]bool)
	for _, str := range wire2 {
		
		direction := str[0]
		magnitude, _ := strconv.Atoi(str[1:])

		var dx vec2

		if direction == 'R' {
			dx = vec2{1, 0}	
		} else if direction == 'L' {
			dx = vec2{-1, 0}	
		} else if direction == 'U' {
			dx = vec2{0, 1}	
		} else if direction == 'D' {
			dx = vec2{0, -1}	
		}

		for ix := 0; ix < magnitude; ix++ {
			w2.x += dx.x
			w2.y += dx.y
			s2[w2] = true
		}

	}

	s_inter := make(map[vec2]bool)

	for key, _ := range s1 {
		if s2[key] == true {
			s_inter[key] = true
		}
	}


	min_distance := 10000

	for value, _ := range s_inter {
		norm := abs(value.x) + abs(value.y)

		if norm < min_distance {
			min_distance = norm
		}

	}

	fmt.Println(min_distance)

	return 0
}

func part2(wire1, wire2 []string) int {
	// fmt.Println(wire[0])
	return 0
}

func parseInput(lines string) ([]string, []string) {
	strValues := strings.Split(lines, "\n")

	var wire1 []string
	wire1 = strings.Split(strValues[0], ",")


	var wire2 []string
	wire2 = strings.Split(strValues[1], ",")

	return wire1, wire2
}

