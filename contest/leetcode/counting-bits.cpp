/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> countBits(int num) {
        vector<int> buf(num + 1);
        buf[0] = 0;
        if (num == 0) {
            return buf;
        }
        buf[1] = 1;
        for (int i = 2; i <= num; i++) {
            int c = (i & 0x1) + buf[i >> 1];
            buf[i] = c;
        }
        return buf;
    }
};
