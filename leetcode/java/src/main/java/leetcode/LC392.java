package leetcode;

import java.util.TreeSet;

public class LC392 {
    class Solution {
        public boolean isSubsequence(String s, String t) {
            TreeSet<Integer>[] chars = new TreeSet[26];
            for (int i = 0; i < 26; i++) {
                chars[i] = new TreeSet<>();
            }
            for (int i = 0; i < t.length(); i++) {
                char c = t.charAt(i);
                chars[c - 'a'].add(i);
            }
            int pos = 0;
            for (char c : s.toCharArray()) {
                TreeSet<Integer> ts = chars[c - 'a'];
                Integer p = ts.ceiling(pos);
                if (p == null) {
                    return false;
                }
                pos = p + 1;
            }
            return true;
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC392().new Solution();
        System.out.println(sol.isSubsequence("abc", "ahbgdc"));
        System.out.println(sol.isSubsequence("axc", "ahbgdc"));
    }
}
