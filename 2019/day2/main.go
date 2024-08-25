package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
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

	fmt.Printf("Part 1: %d\n", part1(input))
	fmt.Printf("Part 2: %d\n", part2(input))
}

type VM struct {
	pc int
	saved_mem []int
	mem []int
}

func vm_init (mem []int ) *VM {

	new_vm := VM{saved_mem: mem}
	new_vm.restart()

	return &new_vm
}

func (vm *VM) restart () {

	vm.mem = make([]int, len(vm.saved_mem))
	copy(vm.mem, vm.saved_mem)
	vm.pc = 0

}

func (vm *VM) run (noun, verb int) int {

	vm.mem[1] = noun 
	vm.mem[2] = verb

	for vm.pc + 4 < len(vm.mem) {
		
		switch vm.mem[vm.pc] {
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

	vm := vm_init(mem)

	return vm.run(12, 2)

}

func part2(mem []int) int {

	vm := vm_init(mem)

	for ix := 0; ix < 100; ix ++ {
		for iy := 0; iy < 100; iy ++ {

			if vm.run(ix, iy) == 19690720 {
				return 100 * ix + iy
			}
			vm.restart()
		}
	}
	return -1
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

