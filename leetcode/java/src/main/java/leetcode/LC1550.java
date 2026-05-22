package leetcode;

public class LC1550 {
    class Solution {
        public boolean threeConsecutiveOdds(int[] arr) {
            int cnt = 0;
            for (int c : arr) {
                if (c % 2 == 1) {
                    cnt += 1;
                    if (cnt == 3) {
                        return true;
                    }
                } else {
                    cnt = 0;
                }
            }
            return false;
        }
    }
}
