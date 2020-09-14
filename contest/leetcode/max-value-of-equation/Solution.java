import java.util.*;

class Solution {
    public int findMaxValueOfEquation(int[][] points, int k) {
        TreeMap<Integer, Integer> tm = new TreeMap();
        int j = 0;
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < points.length; i++) {
            while ((points[i][0] - points[j][0]) > k) {
                int diff = points[j][1] - points[j][0];
                Integer j2 = tm.get(diff);
                if ((j2 != null) && (j2 == j)) {
                    tm.remove(diff);
                }
                j += 1;
            }
            if (tm.size() != 0) {
                int last = tm.lastKey();
                ans = Math.max(ans, last + points[i][1] + points[i][0]);
            }
            tm.put(points[i][1] - points[i][0], i);
        }
        return ans;
    }
}