import java.util.*;

class PairInteger implements Comparable<PairInteger>{
    int value;
    int idx;
    public PairInteger(int value, int idx) {
        this.value = value;
        this.idx = idx;
    }
    public int compareTo(PairInteger o) {
        if (this.value == o.value) {
            return this.idx - o.idx;
        }
        return this.value - o.value;
    }
}
class Solution{
    public int longestSubarray(int[] nums, int limit) {
        TreeSet<PairInteger> ts = new TreeSet();
        int j = 0;
        int ans = 0;
        for(int i=0;i<nums.length;i++) {
            PairInteger pi = new PairInteger(nums[i], i);
            ts.add(pi);
            while (j <= i) {
                PairInteger max = ts.last();
                PairInteger min = ts.first();
                if ((max.value - min.value) <= limit) {
                    ans = Math.max(ans, ts.size());
                    break;
                } else {
                    ts.remove(new PairInteger(nums[j], j));
                    j += 1;
                }
            }
        }
        return ans;
    }
}