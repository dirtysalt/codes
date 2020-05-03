/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <cassert>
#include <vector>
using namespace std;

class Solution {
   public:
    bool isOneBitCharacter(vector<int>& bits) {
        for (int i = 0; i < bits.size();) {
            if (bits[i] == 1) {
                i += 2;
                if (i >= bits.size()) return false;
            } else {
                i += 1;
                if (i == bits.size()) return true;
            }
        }
        assert(false);
        return false;
    }
};
