/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
using namespace std;

class Solution {
   public:
    void nextPermutation(vector<int>& nums) {
        if (nums.size() == 0) return;
        // find swap position.
        int i = nums.size() - 1;
        for (; i >= 1; i--) {
            if (nums[i] > nums[i - 1]) {
                break;
            }
        }
        if (i == 0) {
            sort(nums.begin(), nums.end());
            return;
        }
        // find another swap position.
        int min_value = nums[i];
        int min_index = i;
        for (int j = i + 1; j < nums.size(); j++) {
            if (nums[j] <= nums[i - 1]) continue;
            if (nums[j] < min_value) {
                min_value = nums[j];
                min_index = j;
            }
        }
        swap(nums[min_index], nums[i - 1]);
        sort(nums.begin() + i, nums.end());
    }
};
