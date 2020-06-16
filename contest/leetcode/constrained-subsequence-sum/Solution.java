import java.util.*;

class Solution {
    public int constrainedSubsetSum(int[] nums, int k) {
        int n = nums.length;
        int[] dp = new int[n];
        TreeMap<Integer, Integer> tm = new TreeMap<>();
        int ans = -(1 << 30);
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int last = 0;
            if (tm.size() != 0) {
                last = tm.lastKey();
            }
            last = Math.max(last, 0);
            int res = x + last;
            dp[i] = res;
            ans = Math.max(ans, res);
            // System.out.println(Arrays.toString(dp));
            // add res
            Integer c = tm.get(res);
            if (c == null)
                c = 0;
            tm.put(res, c + 1);
            if (i >= k) {
                res = dp[i - k];
                c = tm.get(res);
                if (c == 1) {
                    tm.remove(res);
                } else {
                    tm.put(res, c - 1);
                }
            }
        }
        return ans;
    }
}
