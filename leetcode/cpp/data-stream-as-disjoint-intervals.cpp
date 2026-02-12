/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */

struct Interval {
    int start;
    int end;
    Interval() : start(0), end(0) {}
    Interval(int s, int e) : start(s), end(e) {}
};
class SummaryRanges {
   public:
    /** Initialize your data structure here. */
    map<int, Interval> end_map;
    map<int, Interval> start_map;

    SummaryRanges() {}

    void addNum(int val) {
        Interval intv(val, val);
        // this interval has been covered or not.
        auto it = end_map.lower_bound(val);
        if (it != end_map.end() && it->second.start <= val) {
            return;
        }

        it = end_map.find(val - 1);
        if (it != end_map.end()) {
            intv.start = it->second.start;
            end_map.erase(it);
            start_map.erase(intv.start);
        }

        it = start_map.find(val + 1);
        if (it != start_map.end()) {
            intv.end = it->second.end;
            start_map.erase(it);
            end_map.erase(intv.end);
        }
        start_map[intv.start] = intv;
        end_map[intv.end] = intv;
    }

    vector<Interval> getIntervals() {
        vector<Interval> res;
        for (auto it = start_map.begin(); it != start_map.end(); ++it) {
            res.push_back(it->second);
        }
        return res;
    }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */