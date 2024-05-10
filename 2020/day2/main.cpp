#include <iostream>
#include <fstream>
#include <chrono>
#include <ranges>

bool is_valid(int lo, int hi, char c, std::string password) {
  auto count = std::ranges::count(password, c);
  return lo <= count && count <= hi; 
}

bool is_valid_2(int ix1, int ix2, char c, std::string password) {
  return (password[ix1 - 1] == c ^ password[ix2 - 1] == c);
}

int part_one() {

  std::ifstream is {"input.txt"};

  int lo, hi;
  std::string letter;
  std::string password;

  int res = 0;

  while (is >> lo >> hi >> letter >> password) {
    hi = -hi;

    if (is_valid(lo, hi, letter[0], password)) {
      ++res;
    }
  }
  return res;
}

int part_two(  ) {
  std::ifstream is {"input.txt"};

  int lo, hi;
  std::string letter;
  std::string password;

  int res = 0;

  while (is >> lo >> hi >> letter >> password) {
    hi = -hi;

    if (is_valid_2(lo, hi, letter[0], password)) {
      ++res;
    }
  }
  return res;
}

int main() {

  auto start = std::chrono::high_resolution_clock::now();

  std::cout << "Part one result: " << part_one() << std::endl;

  auto stop = std::chrono::high_resolution_clock::now();

  auto duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by part one: "
  << duration.count() << " microseconds" << std::endl;


  start = std::chrono::high_resolution_clock::now();

  std::cout << "Part one result: " << part_two() << std::endl;

  stop = std::chrono::high_resolution_clock::now();

  duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by part two: "
  << duration.count() << " microseconds" << std::endl;
}


