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

class Solution {
   public:
    int shortestPathLength(vector<vector<int>>& graph) {
        set<int> visited;
        queue<pair<int, int>> Q;
        int n = graph.size();
        for (int i = 0; i < n; i++) {
            int st = (1 << (i + 12)) + (1 << i);
            visited.insert(st);
            Q.push({st, 0});
        }
        while (!Q.empty()) {
            pair<int, int> item = Q.front();
            Q.pop();
            int st = item.first;
            int cost = item.second;
            int pos = 0;
            for (int i = 0; i < 12; i++) {
                if ((st >> (i + 12)) & 0x1) {
                    pos = i;
                    break;
                }
            }
            st = st & ((1 << 12) - 1);
            if (st == ((1 << n) - 1)) {
                return cost;
            }
            for (int nb : graph[pos]) {
                int new_st = (1 << (12 + nb)) | st | (1 << nb);
                if (visited.find(new_st) == visited.end()) {
                    visited.insert(new_st);
                    Q.push({new_st, cost + 1});
                }
            }
        }
        return -1;
    }
};