/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <map>
#include <set>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> ans(findNums.size());
        map<int, int> finds;

        for (int i = 0; i < findNums.size(); i++) {
            finds[findNums[i]] = i;
        }
        for (int i = nums.size() - 1; i >= 0; i--) {
            int x = nums[i];
            auto it = finds.find(x);
            if (it == finds.end()) continue;
            int xpos = it->second;

            int value = -1;
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] > x) {
                    value = nums[j];
                    break;
                }
            }
            ans[xpos] = value;
        }
        return ans;
    }
};