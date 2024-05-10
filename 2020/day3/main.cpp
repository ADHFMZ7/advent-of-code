#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

#define FILENAME "input.txt"

int calculate_slope(int drow, int dcol, std::vector<std::string>& vc) {


  int res = 0;

  int col = 0;
  std::string row;

  for (int ix = 0; ix < vc.size(); ix += drow) {
    row = vc[ix];

    if (row[col % row.length()] == '#') {
      ++res;
    }
    col += dcol;
  }
  return res;
}

int part_one(std::vector<std::string>& vc) {

  // int col = 0;
  // int res = 0;
  //
  // for (auto row : vc) {
  //   
  //   if (row[col % row.length()] == '#') {
  //     ++res; 
  //   }
  //
  //   col += 3;
  // }

  return calculate_slope(1, 3, vc);
}

unsigned long long part_two(std::vector<std::string> vc) {

  unsigned long long res = 1;

  res *= calculate_slope(1, 1, vc);
  res *= calculate_slope(1, 3, vc);
  res *= calculate_slope(1, 5, vc);
  res *= calculate_slope(1, 7, vc);
  res *= calculate_slope(2, 1, vc);
  return res;

}

int main() {

  std::ifstream is {FILENAME};

  std::vector<std::string> vc;
  std::string line;

  while (is >> line) {

    vc.emplace_back(line); 

  }

  auto start = std::chrono::high_resolution_clock::now();

  std::cout << "Part one: " << part_one(vc) << std::endl;

  auto stop = std::chrono::high_resolution_clock::now();

  auto duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by part one: "
  << duration.count() << " microseconds" << std::endl;


  start = std::chrono::high_resolution_clock::now();

  std::cout << "Part two: " << part_two(vc) << std::endl;

  stop = std::chrono::high_resolution_clock::now();

  duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by part two: "
  << duration.count() << " microseconds" << std::endl;



}


