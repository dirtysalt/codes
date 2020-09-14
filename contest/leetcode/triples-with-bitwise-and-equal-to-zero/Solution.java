import java.util.*;

class Solution {
    public int countTriplets(int[] A) {
        int n = A.length;
        TreeMap<Integer, Integer> cnt = new TreeMap();
        for (int i=0;i<n;i++) {
            for (int j =0;j<n;j++) {
                int x = A[i] & A[j];
                Integer c = cnt.get(x);
                if (c == null) {
                    c = 0;
                }
                cnt.put(x, c + 1);
            }
        }
        int ans = 0;
        for(int i=0;i<n;i++) {
            int x = A[i];
            for(Map.Entry<Integer,Integer> e: cnt.entrySet()) {
                if ((x & e.getKey()) == 0) {
                    ans += e.getValue();
                }
            }
        }
        return ans;
    }
}