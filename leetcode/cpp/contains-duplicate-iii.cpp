#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

template <typename T1, typename T2> string print_map(map<T1, T2> &m) {
  ostringstream oss;
  oss << "map[";
  for (auto it = m.begin(); it != m.end(); ++it) {
    oss << "(" << it->first << "," << it->second << ") ";
  }
  oss << "]";
  return oss.str();
}

template <typename T1> string print_set(set<T1> &m) {
  ostringstream oss;
  oss << "set[";
  for (auto it = m.begin(); it != m.end(); ++it) {
    oss << *it << " ";
  }
  oss << "]";
  return oss.str();
}

class Solution {
public:
  bool containsNearbyAlmostDuplicate(vector<int> &nums, int k, int t) {
    map<long long, int> past; // 这里past当做set来用
    map<uint, int> values;
    if (t < 0) {
      return false;
    }

    int j = 0;
    for (int i = 0; i < nums.size(); i++) {
      if ((i - j) > k) {
        // remove nums[j]
        int x = nums[j];
        auto it = past.lower_bound(x);
        assert(it != past.end());
        if (it != past.begin()) {
          --it;
          int d = abs(it->first - x);
          values[d] -= 1;
          if (values[d] == 0) {
            values.erase(d);
          }
        }

        it = past.lower_bound(x);
        assert(it != past.end());
        if ((++it) != past.end()) {
          int d = abs(it->first - x);
          values[d] -= 1;
          if (values[d] == 0) {
            values.erase(d);
          }
        }

        past.erase(x);
        j += 1;
      }

      // insert nums[i];
      int x = nums[i];
      if (past[x] != 0) {
        return true;
      }
      past[x] += 1;

      auto it = past.lower_bound(x);
      assert(it != past.end());
      if (it != past.begin()) {
        --it;
        int d = abs(it->first - x);
        values[d] += 1;
      }
      it = past.lower_bound(x);
      assert(it != past.end());
      if ((++it) != past.end()) {
        int d = abs(it->first - x);
        values[d] += 1;
      }

      // cout << "================" << endl;
      // cout << "past and values" << endl;
      // cout << "past = " << print_map(past) << endl;
      // cout << "values = " << print_map(values) << endl;

      // check abs values.
      auto it2 = values.begin();
      if (it2 != values.end() and it2->first <= t) {
        return true;
      }
    }
    return false;
  }
};

int main() {
  auto sol = Solution();
  vector<tuple<vector<int>, int, int, bool>> cases = {
      {vector<int>{1, 5, 9, 1, 5, 9}, 2, 3, false},
      {vector<int>{1, 2, 3, 1}, 3, 0, true},
      {vector<int>{-1, -1}, 1, - 1, false},
      {vector<int>{-1,2147483647},1,2147483647, false},
      {vector<int>{2147483647,-2147483647},1,2147483647, false},
  };

  for (int i = 0; i < cases.size(); i++) {
    auto &c = cases[i];
    auto exp = std::get<3>(c);
    auto res = sol.containsNearbyAlmostDuplicate(std::get<0>(c), std::get<1>(c),
                                                 std::get<2>(c));
    if (exp != res) {
      cout << "case #" << i << " failed. exp=" << exp << ", res=" << res
           << endl;
    } else {
      cout << "case #" << i << " PASSED!!!" << endl;
    }
  }
  return 0;
}