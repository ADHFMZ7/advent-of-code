#include <iostream>
#include <chrono>

int solution() {

  int sum = 0;

  for (int ix = 0; ix < 1000; ++ix) {
    if (ix % 5 == 0 || ix % 3 == 0)  {
      sum += ix;
    }
  }
  return sum;
}

int main() {

  int answer;

  auto start = std::chrono::high_resolution_clock::now();

  answer = solution();

  auto stop = std::chrono::high_resolution_clock::now();

  auto duration = duration_cast<std::chrono::microseconds>(stop - start);

  std::cout << "Answer: " << answer << std::endl;

  std::cout << "Time taken by function: "
  << duration.count() << " microseconds" << std::endl;


}
