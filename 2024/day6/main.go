package main

import (
  "fmt";
  "os";
  "strings";
)

type Point struct {
  x, y int
}

func (p1 Point) add(p2 Point) Point {
  return Point{x: p1.x + p2.x, y: p1.y + p2.y} 
}

func (p1 Point) in_grid(r, c int) bool {
  return 0 <= p1.x && p1.x < r &&
         0 <= p1.y && p1.y < c;
        
}

func (p1 *Point) change_dir() {
  if p1.x == 0 && p1.y == -1 {
    p1.x = -1
    p1.y = 0
  } else if p1.x == 0 && p1.y == 1 {
    p1.x = 1
    p1.y = 0
  } else {
    temp := p1.x
    p1.x = -p1.y
    p1.y = -temp
  }
}

func main() {

  dat, _ := os.ReadFile("./input")
  grid := strings.Split(string(dat), "\n")

  m := make(map[Point]int)

  R, C := len(grid), len(grid[0])

  // Part 1
  res := 0
  var p Point
  dp := Point{x:-1, y:0}

  for r := range grid {
    for c := range grid[r] {
      pc := Point{x:r, y:c}
      char := grid[r][c]

      if char == '^' {
        m[pc] = 0
        p = pc
      } else if char == '#' {
        m[pc] = 1
      }
    }
  }

  for p.add(dp).in_grid(R, C) {
    if m[p] == 0 {
      res += 1
      m[p] = 3
    }


    if m[p.add(dp)] == 1 {
      dp.change_dir()
      continue
    }
  
    p = p.add(dp)
  }

  fmt.Printf("Part 1: %d\n", res)
  
  // Part 2


  fmt.Printf("Part 2: %d\n", res)
}
