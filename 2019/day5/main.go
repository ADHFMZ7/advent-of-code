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

	fmt.Printf("Part 1: \n", ); part1(input)
	fmt.Printf("Part 2: \n", ); part2(input)
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

func (vm *VM) read_params(num_params int, modes [3]int) []int {

	out := []int{0, 0, 0}
	for ix, mode := range modes[:num_params] {
		if ix == 2{
			out[ix] = vm.mem[vm.pc + ix + 1]
		} else if mode == 0 {
			out[ix] = vm.mem[vm.mem[vm.pc+ix+1]]
		} else if mode == 1 {
			out[ix] = vm.mem[vm.pc + ix + 1]
		}
	}
	return out
}

func (vm *VM) run (noun, verb int) int {

	vm.mem[1] = noun 
	vm.mem[2] = verb

	for {
	
		opcode := vm.mem[vm.pc] % 100
		param_modes := vm.mem[vm.pc] / 100
		
		var p [3]int

		p[0] = param_modes % 10
		p[1] = param_modes % 100 / 10
		p[2] = param_modes % 1000 / 100

		var num_params int

		switch opcode {
			case 1:
				num_params = 3
				params := vm.read_params(num_params, p)

				vm.mem[params[2]] = params[0] + params[1]
			case 2:
				num_params = 3
				params := vm.read_params(num_params, p)
				vm.mem[params[2]] = params[0] * params[1]
			case 3:
				num_params = 1
				fmt.Print("input: ")
				var num int
				fmt.Scanf("%d", &num)
				vm.mem[vm.mem[vm.pc + 1]] = num

			case 4:
				num_params = 1
				params := vm.read_params(num_params, p)
				fmt.Printf("output: %d\n", params[0])

			case 5:
				num_params = 2
				params := vm.read_params(num_params, p)
				if params[0] != 0 {
					vm.pc = params[1] - num_params - 1
				}
				
			case 6:
				num_params = 2
				params := vm.read_params(num_params, p)
				if params[0] == 0 {
					vm.pc = params[1] - num_params - 1
				}

			case 7:
				num_params = 3
				params := vm.read_params(num_params, p)
				if params[0] < params[1] {
					vm.mem[params[2]] = 1
				} else {
					vm.mem[params[2]] = 0
				}

			case 8:
				num_params = 3
				params := vm.read_params(num_params, p)
				if params[0] == params[1] {
					vm.mem[params[2]] = 1
				} else {
					vm.mem[params[2]] = 0
				}

			case 99:
				return vm.mem[0]
		}
		vm.pc += (num_params + 1)
	}

	return vm.mem[0]
}


func part1(mem []int) int {
	vm := vm_init(mem)

	vm.run(vm.mem[1], vm.mem[2])

	return 0
}

func part2(mem []int) int {
	vm := vm_init(mem)

	vm.run(vm.mem[1], vm.mem[2])

	return 0

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


