package main

import (
	"fmt"
	"strconv"
)

func main() {

	fmt.Printf("Part 1: %d\n", part1(128392, 643281))
	fmt.Printf("Part 2: %d\n", part2(128392, 643281))

}

func follows_rule1(num, start, end int) bool {

	if num < 99999 || num > 999999 || num < start || num > end {
		return false
	}

	same_found := false

	numstr := strconv.Itoa(num)
	
	for ix, digit := range strconv.Itoa(num) {

		if ix >= 1 && numstr[ix - 1] == byte(digit) {
			same_found = true
		}
		if ix >= 1 && numstr[ix - 1] > byte(digit) {
			return false
		}
	}
	return same_found

}

func follows_rule2(num, start, end int) bool {

	if num < 99999 || num > 999999 || num < start || num > end {
		return false
	}

	counts := make(map[rune]int)

	numstr := strconv.Itoa(num)
	
	for ix, digit := range strconv.Itoa(num) {

		counts[digit] = counts[digit] + 1

		if ix >= 1 && numstr[ix - 1] > byte(digit) {
			return false
		}
	}

	for _, value := range counts {
		if value == 2 {
			return true
		}
	}
	return false

}

func part1(start, end int) int {

	res := 0

	for ix := start; ix < end; ix++ {
		if follows_rule1(ix, start, end) {
			res += 1
		}
	}

	return res
}

func part2(start, end int) int {
	res := 0

	for ix := start; ix < end; ix++ {
		if follows_rule2(ix, start, end) {
			res += 1
		}
	}

	return res
}
