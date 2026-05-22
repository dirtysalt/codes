package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Map;
import java.util.TreeMap;

public class LC239 {
    class Solution {
        public int[] maxSlidingWindow(int[] nums, int k) {
            TreeMap<Integer, Integer> tm = new TreeMap<>();
            for (int i = 0; i < k - 1; i++) {
                int x = nums[i];
                tm.put(x, i);
            }
            ArrayList<Integer> tmp = new ArrayList<>();
            for (int i = k - 1; i < nums.length; i++) {
                int x = nums[i];
                tm.put(x, i);

                Map.Entry<Integer, Integer> last = tm.lastEntry();
                tmp.add(last.getKey());

                int p = i + 1 - k;
                x = nums[p];
                if (tm.get(x) == p) {
                    tm.remove(x);
                }
            }
            int[] ans = tmp.stream().mapToInt(x -> x).toArray();
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC239().new Solution();
        {
            int nums[] = {1, 3, -1, -3, 5, 3, 6, 7};
            System.out.println(Arrays.toString(sol.maxSlidingWindow(nums, 3)));
        }
    }
}
