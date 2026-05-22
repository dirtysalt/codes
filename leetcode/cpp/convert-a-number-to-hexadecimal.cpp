/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <string>
using namespace std;

class Solution {
   public:
    string toHex(int num) {
        if (num == 0) return "0";
        string ans = "";
        bool leading = true;
        for (int i = 7; i >= 0; i--) {
            int val = 0;
            for (int j = 3; j >= 0; j--) {
                val = val * 2;
                if ((num >> (i * 4 + j)) & 0x1) {
                    val += 1;
                }
            }
            if (val == 0 && leading) continue;
            leading = false;
            if (val < 10)
                ans += ('0' + val);
            else
                ans += ('a' + val - 10);
        }
        return ans;
    }
};