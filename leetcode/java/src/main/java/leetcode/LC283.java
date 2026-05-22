package leetcode;

public class LC283 {
    class Solution {
        public void moveZeroes(int[] nums) {
            int j = 0;
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] != 0) {
                    nums[j] = nums[i];
                    j += 1;
                }
            }
            while (j < nums.length) {
                nums[j] = 0;
                j += 1;
            }
        }
    }
}
