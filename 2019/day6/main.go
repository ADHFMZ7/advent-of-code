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

	// fmt.Printf("Part 1: %d\n", part1(orbits))
	fmt.Printf("Part 2: %d\n", part2(orbits))

}

func enqueue(queue []obj, element obj) []obj{
    queue = append(queue, element) // Simply append to enqueue.
    fmt.Println("Enqueued:", element)
    return queue
}

func dequeue(queue []obj) (obj, []obj) {
	element := queue[0] // The first element is the one to be dequeued. 
	if len(queue) == 1 { 
		var tmp = []obj{} 
		return element, tmp 
	} 
	return element, queue[1:] // Slice off the element once it is dequeued. 
}

func part1(orbits map[string][]string) int {


	var dfs func(name string) int

	dfs = func (name string) int {

		children, ok := orbits[name]

		if !ok {
			return 0
		}

		child_sum := 0

		for _, child := range children{
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

type obj struct {
	name string
	count int
}

func part2(orbits map[string][]string) int {

	// now we have bidirectional tree, so we just do a bfs

	var q []obj
	q = enqueue(q, obj{"YOU", 0})
	var elem obj
	v := make (map[string]bool)

		

	for len(q) > 0 {
		elem, q = dequeue(q)

		if elem.name == "SAN" {
			return elem.count - 2
		}

		v[elem.name] = true
		
		children := orbits[elem.name]

		for _, child := range children {
			if !v[child]{
				q = enqueue(q, obj{child, elem.count + 1})
			}
		}
		


	}
	return -1
}

func parseInput(text string) (map[string][]string) {
	lines := strings.Split(strings.TrimSuffix(text, "\n"), "\n")

	ret := make(map[string][]string)

	for _, line := range lines {
		vals := strings.Split(line, ")")
		

		if children, in_map := ret[vals[0]]; in_map {

			children = append(children, vals[1])
			ret[vals[0]] = children

			ret[vals[1]] = append(ret[vals[1]], vals[0])

		} else {
			ret[vals[0]] = []string{vals[1]}
			ret[vals[1]] = append(ret[vals[1]], vals[0])
		}

	}

	return ret 
}
