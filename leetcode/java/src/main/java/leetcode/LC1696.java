package leetcode;

import java.util.TreeMap;

public class LC1696 {
    class Solution {
        public int maxResult(int[] nums, int k) {
            int[] maxValue = new int[nums.length];
            TreeMap<Integer, Integer> tm = new TreeMap<>();
            tm.put(nums[0], 1);
            maxValue[0] = nums[0];
            for (int i = 1; i < nums.length; i++) {
                int last = tm.lastKey();
                maxValue[i] = last + nums[i];
                if ((i - k) >= 0) {
                    int x = maxValue[i - k];
                    Integer ref = tm.get(x);
                    if (ref == 1) {
                        tm.remove(x);
                    } else {
                        tm.put(x, ref - 1);
                    }
                }
                if (true) {
                    int x = maxValue[i];
                    Integer ref = tm.get(x);
                    if (ref == null) {
                        tm.put(x, 1);
                    } else {
                        tm.put(x, ref + 1);
                    }
                }
            }
            return maxValue[maxValue.length - 1];
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC1696().new Solution();
        {
            int[] nums = {1, -1, -2, 4, -7, 3};
            System.out.println(sol.maxResult(nums, 2));
        }
        {
            int[] nums = {10, -5, -2, 4, 0, 3};
            System.out.println(sol.maxResult(nums, 3));
        }
    }
}
