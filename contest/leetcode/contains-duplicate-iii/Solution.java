import java.util.*;

class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        TreeSet<Integer> set = new TreeSet<>();
        for(int i = 0; i < nums.length;i ++ ) {
            int x = nums[i];
            Integer g = set.ceiling(x);
            if (g != null && ((long)g - x) <= t) {
                return true;
            }
            Integer l = set.floor(x);
            if (l != null && ((long)x - l) <= t) {
                return true;
            }
            set.add(x);
            if (set.size() > k) {
                set.remove(nums[i-k]);
            }
        }
        return false;
    }
}

