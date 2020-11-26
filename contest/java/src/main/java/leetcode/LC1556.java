package leetcode;

public class LC1556 {
    class Solution {
        public String thousandSeparator(int n) {
            if (n == 0) {
                return "0";
            }
            StringBuffer sb = new StringBuffer();
            int p = 1;
            while (n != 0) {
                int x = n % 10;
                n = n / 10;
                sb.append((char) (x + '0'));
                if ((p % 3 == 0) & (n != 0)) {
                    sb.append('.');
                }
                p += 1;
            }
            sb.reverse();
            String ans = sb.toString();
            return ans;
        }
    }

    public static void main(String[] args) {
        Solution sol = new LC1556().new Solution();
        System.out.println(sol.thousandSeparator(123456789));
        System.out.println(sol.thousandSeparator(0));
    }
}
