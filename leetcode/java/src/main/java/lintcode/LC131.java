package lintcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeSet;

// https://www.lintcode.com/problem/the-skyline-problem/

class LC131 {
    public class Solution {
        class Event implements Comparable<Event> {
            int in;
            int x;
            int h;
            int idx;

            public Event(int in, int x, int h, int idx) {
                this.in = in;
                this.x = x;
                this.h = h;
                this.idx = idx;
            }

            public int compareTo(Event it) {
                return x - it.x;
            }
        }

        class Building implements Comparable<Building> {
            int h;
            int idx;

            public Building(int h, int idx) {
                this.h = h;
                this.idx = idx;
            }

            public int compareTo(Building it) {
                if (this.h != it.h) {
                    return this.h - it.h;
                }
                return this.idx - it.idx;
            }
        }


        /**
         * @param buildings: A list of lists of integers
         * @return: Find the outline of those buildings
         */
        public List<List<Integer>> buildingOutline(int[][] buildings) {
            // write your code here
            int n = buildings.length;
            List<List<Integer>> ans = new ArrayList<>();
            if (n == 0) {
                return ans;
            }

            Event[] events = new Event[2 * n];
            for (int i = 0; i < n; i++) {
                events[2 * i] = new Event(0, buildings[i][0], buildings[i][2], i);
                events[2 * i + 1] = new Event(1, buildings[i][1], buildings[i][2], i);
            }
            Arrays.sort(events);

            TreeSet<Building> ts = new TreeSet<>();
            int cur = 0;

            for (int i = 0; i < events.length; i++) {
                Event ev = events[i];
                int h = 0;
                if (ts.size() > 0) {
                    h = ts.last().h;
                }
                if (ev.in == 0) {
                    if ((h < ev.h) && (ev.x > cur)) {
                        if (h != 0) {
                            ArrayList<Integer> t = new ArrayList();
                            t.add(cur);
                            t.add(ev.x);
                            t.add(h);
                            ans.add(t);
                        }
                        cur = ev.x;
                    }
                    ts.add(new Building(ev.h, ev.idx));
                } else {
                    if ((h == ev.h) && (ev.x > cur)) {
                        ArrayList<Integer> t = new ArrayList();
                        t.add(cur);
                        t.add(ev.x);
                        t.add(h);
                        cur = ev.x;
                        ans.add(t);
                    }
                    ts.remove(new Building(ev.h, ev.idx));
                }
            }

            List<List<Integer>> res = new ArrayList<>();
            for (int i = 0; i < ans.size(); i++) {
                int j = res.size();
                List<Integer> x = ans.get(i);
                if (j > 0) {
                    List<Integer> p = res.get(j - 1);
                    if (p.get(2).equals(x.get(2)) && p.get(1).equals(x.get(0))) {
                        p.set(1, x.get(1));
                        // System.out.println("!!!!");
                        continue;
                    }
                }
                res.add(x);
            }

            return res;
        }
    }
}