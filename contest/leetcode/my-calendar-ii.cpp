/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;

class MyCalendarTwo {
   public:
    map<int, int> counter;
    MyCalendarTwo() {}

    bool book(int start, int end) {
        counter[start] += 1;
        counter[end] -= 1;
        int overlap = 0;
        auto ans = true;
        for (auto it : counter) {
            overlap += it.second;
            if (overlap >= 3) {
                ans = false;
                break;
            }
        }
        if (!ans) {
            counter[start] -= 1;
            counter[end] += 1;
        }
        return ans;
    }
};