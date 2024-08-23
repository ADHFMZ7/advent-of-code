package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Read the input file
	file, err := os.Open("input")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var input []int
	for scanner.Scan() {
		line := scanner.Text()
		input = parseInput(line)
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	// Process the input
	fmt.Printf("Part 1: %d\n", part1(input))
	part2(input)
}

type VM struct {
	PC int
	mem []int
}

func vm_init (mem []int) {

	


	pc := 0

}

func (VM vm) run (noun, verb int) {

	vm.mem[1] = noun 
	vm.mem[2] = verb

	for vm.pc + 4 < len(vm.mem) {
		
		switch mem[pc] {
			case 1:
				vm.mem[vm.mem[vm.pc + 3]] = vm.mem[vm.mem[vm.pc+1]] + vm.mem[vm.mem[vm.pc+2]]
			case 2:
				vm.mem[vm.mem[vm.pc + 3]] = vm.mem[vm.mem[vm.pc+1]] * vm.mem[vm.mem[vm.pc+2]]
			case 99:
				break
		}
		vm.pc += 4
	}

	return vm.mem[0]
}


func part1(mem []int) int {

	vm := 

	mem[1] = 12
	mem[2] = 2

}

func part2(mem []int) {

	
	




}

func parseInput(line string) []int {
	// Split the input line by commas
	strValues := strings.Split(line, ",")
	var result []int

	for _, str := range strValues {
		num, err := strconv.Atoi(str)
		if err != nil {
			panic(err)
		}
		result = append(result, num)
	}

	return result
}

