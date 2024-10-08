package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {

	content, err := os.ReadFile("input")
	if err != nil {
		panic(err)
	}


	orbits := parseInput(string(content))

	fmt.Printf("Part 1: %d\n", part1(orbits))
	fmt.Printf("Part 2: %d\n", part2(orbits))

}

type Orbit struct {
	parent string
	children []string
}

func part1(orbits map[string]Orbit) int {


	var dfs func(name string) int

	dfs = func (name string) int {

		orbit, ok := orbits[name]

		if !ok {
			return 0
		}

		child_sum := 0

		for _, child := range orbit.children {
			child_sum += dfs(child)
			child_sum += 1
		}
		return child_sum 
		
	}

	ret := 0

	for parent, _ := range orbits {
		ret += dfs(parent)	
	}
	return ret
}

func part2(orbits map[string]Orbit) int {

	return 0
}

func parseInput(text string) (map[string]Orbit) {
	lines := strings.Split(strings.TrimSuffix(text, "\n"), "\n")

	ret := make(map[string]Orbit)

	for _, line := range lines {
		vals := strings.Split(line, ")")
		

		if orbit, in_map := ret[vals[0]]; in_map {

			orbit.children = append(orbit.children, vals[1])
			ret[vals[0]] = orbit

		} else {
			ret[vals[0]] = Orbit{vals[0], []string{vals[1]}}
		}

	}

	return ret 
}
