import java.util.*;

class Solution {
    public boolean find132pattern(int[] nums) {
        if (nums.length == 0) {
            return false;
        }
        TreeSet<Integer> ks = new TreeSet<>();
        Integer[] xs = new Integer[nums.length];

        for (int i= nums.length-1;i>=0;i--) {
            Integer k = ks.floor(nums[i]-1);
            xs[i] = k;
            ks.add(nums[i]);
        }
        System.out.println(Arrays.toString(xs));

        int x = nums[0];
        for(int i=0;i<nums.length-1;i++) {
            x = Math.min(nums[i], x);
            if ((xs[i] != null) && (x < xs[i])) {
                return true;
            }
        }
        return false;
    }

    // public static void main(String[] args) {
    //     Solution sol = new Solution();
    //     int []nums = {3,1,4,2};
    //     System.out.println(sol.find132pattern(nums));
    // }
}
