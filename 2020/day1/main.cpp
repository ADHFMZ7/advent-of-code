#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

//
//
//
//

int main() {

  std::ifstream myfile {"input.txt"};
  int cur_num;
  std::string line;

  std::vector<int> vc;

  while (myfile >> cur_num) {

    vc.emplace_back(cur_num);

  }

  std::for_each(vc.begin(), vc.end(), 
                [] (int i) -> void {std::cout << i << std::endl;}
                );


}

