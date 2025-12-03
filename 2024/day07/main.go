package main

import (
  "fmt";
  "os";
  "strings";
  "strconv"
)
  

func bt(nums []int, total int) int {
  
  if 

  return 0
}

func main() {

  dat, _ := os.ReadFile("./inputtest")
  lines := strings.Split(string(dat), "\n")

  for _, line := range lines[:len(lines)-1] {
    nums := make([]int, 0)
    for ix, num := range strings.Split(line, " ") {
      if ix == 0 {
        a, _ := strconv.Atoi(num[:len(num)-1])
        nums = append(nums, a)
        continue
      }
      a, _ := strconv.Atoi(num)
      nums = append(nums, a)
    }

    total := nums[0]

    for _, num := range nums[1:] {
      fmt.Println(num)
    }

    
    



    break


  }

  fmt.Println()
  // Part 1
  res := 0
  
  fmt.Printf("Part 1: %d\n", res)
  
  // Part 2


  fmt.Printf("Part 2: %d\n", res)
}
