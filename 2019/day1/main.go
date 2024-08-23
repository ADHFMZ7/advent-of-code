package main

import (
  "math";
  "fmt";
  "os";
  "strings";
  "strconv"
)

func calculate_fuel(mass int) int {

  fuel :=  int(math.Floor(float64(mass) /3) - 2)
  if fuel <= 0 {
    return 0
  }

  return fuel + calculate_fuel(fuel)
}
  

func main() {

  // Part 1
  dat, _ := os.ReadFile("./input")
  masses := strings.Split(string(dat), "\n");

  res := 0

  for _, mass := range masses{

    temp, _ := strconv.Atoi(mass)
    res += int(math.Floor( float64(temp) / 3) - 2)
  }
  
  fmt.Printf("Part 1: %d\n", res);
  
  // Part 2

  res = 0

  for _, mass := range masses{
    temp, _ := strconv.Atoi(mass)
    res += calculate_fuel(temp)
  }

  fmt.Printf("Part 2: %d\n", res);
}
