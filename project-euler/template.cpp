#include <iostream>
#include <chrono>

int solution() {
	return 0;
}

int main() {

  auto start = std::chrono::high_resolution_clock::now();

  solution();

  auto stop = std::chrono::high_resolution_clock::now();

  auto duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Time taken by function: "
  << duration.count() << " microseconds" << std::endl;
}
