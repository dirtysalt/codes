import java.util.*;

class Solution {
    public int[] avoidFlood(int[] rains) {
        int n = rains.length;
        TreeSet<Integer> drain = new TreeSet();
        TreeMap<Integer, Integer> fill = new TreeMap();
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = -1;
        }

        boolean ok = true;
        for (int i = 0; i < n; i++) {
            int x = rains[i];
            if (x == 0) {
                drain.add(i);
            } else {
                Integer pos = fill.get(x);
                if (pos != null) {
                    Integer t = drain.higher(pos);
                    if (t == null) {
                        ok = false;
                        break;
                    } else {
                        ans[t] = x;
                        drain.remove(t);
                    }
                }
                fill.put(x, i);
            }
        }
        if (!ok) {
            return new int[0];
        }
        for (Integer x : drain) {
            ans[x] = 1;
        }
        return ans;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] rains = { 2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2 };
        System.out.println(Arrays.toString(sol.avoidFlood(rains)));
    }
}