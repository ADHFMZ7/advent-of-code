#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>

int part_one(  ) {

  return 0;
}

int part_two(  ) {

  return 0;
}

int main() {

  std::ifstream is {"input.txt"};

  int cur_num;
  std::vector<int> vc;

  while (is >> cur_num) {

    vc.emplace_back(cur_num); 

  }


  auto start = std::chrono::high_resolution_clock::now();

  part_one();

  auto stop = std::chrono::high_resolution_clock::now();

  auto duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by part one: "
  << duration.count() << " microseconds" << std::endl;


  start = std::chrono::high_resolution_clock::now();

  part_two();

  stop = std::chrono::high_resolution_clock::now();

  duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by part two: "
  << duration.count() << " microseconds" << std::endl;



}


