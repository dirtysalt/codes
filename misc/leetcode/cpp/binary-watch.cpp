/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cstdio>
#include <string>
#include <vector>
using namespace std;

class Solution {
   public:
    int bits(int v) {
        int c = 0;
        while (v) {
            c += (v & 0x1);
            v = v >> 1;
        }
        return c;
    }
    void solve(int num, vector<string>& result) {
        for (int h = 0; h < 12; h++) {
            for (int m = 0; m < 60; m++) {
                if ((bits(h) + bits(m)) == num) {
                    char buf[10];
                    snprintf(buf, sizeof(buf), "%d:%02d", h, m);
                    string s(buf);
                    result.push_back(s);
                }
            }
        }
    }
    vector<string> readBinaryWatch(int num) {
        vector<string> result;
        solve(num, result);
        return result;
    }
};
