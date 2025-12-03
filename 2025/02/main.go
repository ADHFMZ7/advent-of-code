package main

import (
	"bufio"
	"bytes"
	"fmt"
	"os"
)

func parse_input() ([]int, error) {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(func(data []byte, atEOF bool) (int, []byte, error) {
		if atEOF && len(data) == 0 {
			return 0, nil, nil // No more data to process
		}
		// Find the index of the next comma
		if i := bytes.IndexByte(data, ','); i >= 0 {
			return i + 1, data[0:i], nil // Return the token before the comma
		}
		// If at EOF and no comma found, return the rest of the data as a token
		if atEOF {
			return len(data), data, nil
		}
		// Request more data if no comma is found and not at EOF
		return 0, nil, nil
	})

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	return nil, nil
}

// func part1() {
//
// }
//
// func part2() {
//
// }

func main() {

	parse_input()

}
