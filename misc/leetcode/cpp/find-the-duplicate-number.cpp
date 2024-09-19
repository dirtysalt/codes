class Solution {
public:
    int test(const vector<int>& nums, int dup) {
        int n = nums.size();
        int le = 0;
        for(int x: nums) {
            if (x <= dup) {
                le += 1;
            }
        }
        if (le <= dup) {
            // dup is impossible.
            // try larger.
            return 1;
        } else {
            return -1;
        }
    }
    int findDuplicate(vector<int>& nums) {
        int n = nums.size() - 1;
        int s = 1, e = n;
        int ans = -1;
        while (s <= e) {
            int dup = s + (e - s) / 2;
            int offset =  test(nums, dup);
            if (offset == 1) {
                s = dup + 1;
            } else {
                e = dup - 1;
            }
        }
        ans = s;
        return ans;
    }
};