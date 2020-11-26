package leetcode;

public class LC1588 {
    class Solution {
        public int sumOddLengthSubarrays(int[] arr) {
            int ans = 0;
            for (int sz = 1; sz <= arr.length; sz += 2) {
                int acc = 0;
                for (int i = 0; i < sz; i++) {
                    acc += arr[i];
                }
                ans += acc;
                for (int i = sz; i < arr.length; i++) {
                    acc += arr[i] - arr[i - sz];
                    ans += acc;
                }
            }
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC1588().new Solution();
        {
            int[] arr = {1, 4, 2, 5, 3};
            System.out.println(sol.sumOddLengthSubarrays(arr));
        }
        {
            int[] arr = {10,11,12};
            System.out.println(sol.sumOddLengthSubarrays(arr));
        }
    }
}
