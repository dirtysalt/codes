package leetcode;

import java.util.TreeSet;

public class LC5616 {
    class Solution {
        public int minimumDeviation(int[] nums) {
            TreeSet<Integer> ts = new TreeSet<>();
            for (int x : nums) {
                if (x % 2 == 0) {
                    ts.add(x);
                } else {
                    ts.add(2 * x);
                }
            }
            int ans = ts.last() - ts.first();
            while (ans > 0 && ts.last() % 2 == 0) {
                int t = ts.last();
                ts.remove(t);
                ts.add(t / 2);
                int off = ts.last() - ts.first();
                ans = Math.min(ans, off);
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC5616().new Solution();
        {
            int[] nums = {1, 2, 3, 4};
            System.out.println(sol.minimumDeviation(nums));
        }
        {
            int[] nums = {4, 1, 5, 20, 3};
            System.out.println(sol.minimumDeviation(nums));
        }
        {
            int[] nums = {2, 10, 8};
            System.out.println(sol.minimumDeviation(nums));
        }
    }
}
