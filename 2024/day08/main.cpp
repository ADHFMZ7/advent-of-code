#include <algorithm>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <format>
#include <iterator>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <utility>

using i32 = uint32_t;
using i64 = uint64_t;

i64 pair_to_key(i32 r, i32 c) {
	return (static_cast<i64>(r) << 32) + c;
}

std::pair<i32, i32> key_to_pair(i64 key) {
	std::pair<i32, i32> ret;
	ret.first = key >> 32;
	ret.second = key % (1 << 31);
	return ret;
}

std::pair<i64, i64> find_antinodes(i64 k1, i64 k2) {

	auto p1 = key_to_pair(k1);
	auto p2 = key_to_pair(k2);

	// std::cout << std::format("{} {} : {} {}\n", p1.first, p1.second, p2.first, p2.second);

	std::pair<i64, i64> ret;

	// i32 dx = std::max(p1.first, p2.first) - std::min(p1.first, p2.first);
	// i32 dy = std::max(p1.second, p2.second) - std::min(p1.second, p2.second);

	i32 dx = p1.first - p2.first;
	i32 dy = p1.second - p2.second;

	if (p1.first + dx == p2.first) ret.first = pair_to_key(p1.first - dx, p1.second - dy);
	else ret.first = pair_to_key(p1.first + dx, p1.second + dy);

	if (p2.first + dx == p1.first) ret.second= pair_to_key(p2.first - dx, p2.second - dy);
	else ret.second = pair_to_key(p2.first + dx, p2.second + dy);

	return ret;
}

bool in_grid(int R, int C, i64 key) {
	auto pair = key_to_pair(key);
	// std::cout << pair.first << "  " << pair.second << std::endl;
	return (0 <= pair.first && pair.first < R) && (0 <= pair.second && pair.second < C);
}

int main() {

	int R, C;

	std::ifstream fi{"input"};

	if (!fi) {
		std::cerr << "Error reading file" << std::endl;
		exit(1);
	}

	std::string inp;
	std::unordered_map<i64, char> map;

	for (i32 r = 0; fi >> inp; ++r) {
		for (i32 c = 0; c < inp.size(); ++c) {
			if (inp[c] != '.') map[pair_to_key(r, c)] = inp[c];
		}
		R = r;
	}
	
	C = inp.size();

	std::unordered_set<i64> visited;

	for (auto i = map.begin(); i != map.end(); ++i) {
		for (auto j = std::next(i); j != map.end(); ++j) {
			if (j->second == i->second) {
				auto a = find_antinodes(i->first, j->first);

				if (in_grid(R, C, a.first)) visited.insert(a.first);
				if (in_grid(R, C, a.second)) visited.insert(a.second);
			}
		}
	}

	// for (auto k : visited) {
	// 	auto pair = key_to_pair(k); 
	// 	std::cout << std::format("{}, {}\n", pair.first, pair.second);
	//  }

	std::cout << visited.size() << std::endl;

	return 0;
}
