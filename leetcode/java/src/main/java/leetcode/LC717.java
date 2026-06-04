package leetcode;

public class LC717 {
    class Solution {
        public boolean isOneBitCharacter(int[] bits) {
            boolean ok = true;
            for (int i = 0; i < bits.length; i++) {
                if (bits[i] == 1) {
                    if ((i + 1) == bits.length) {
                        return false;
                    }
                    i++;
                    ok = false;
                } else {
                    ok = true;
                }
            }
            return ok;
        }
    }
}
