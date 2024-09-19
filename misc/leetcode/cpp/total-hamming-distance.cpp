/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    int totalHammingDistance(vector<int>& nums) {
        int bits[32] = {0};
        for (int k = 0; k < nums.size(); k++) {
            int n = nums[k];
            for (int p = 0; p < 32; p++) {
                if (n & (1 << p)) {
                    bits[p] += 1;
                }
            }
        }
        int count = 0;
        for (int p = 0; p < 32; p++) {
            count += (nums.size() - bits[p]) * bits[p];
        }
        return count;
    }
};
