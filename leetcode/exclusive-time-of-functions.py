#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        st = []
        times = [0] * n
        for log in logs:
            (func_id, action, ts) = log.split(':')
            func_id = int(func_id)
            ts = int(ts)

            if action == 'start':
                if st:
                    xid, xts = st[-1]
                    times[xid] += (ts - xts)
                st.append((func_id, ts))

            else:
                xid, xts = st[-1]
                st.pop()
                assert func_id == xid
                times[xid] += (ts - xts + 1)

                if st:
                    xid, _ = st[-1]
                    st.pop()
                    st.append((xid, ts + 1))
        return times


if __name__ == '__main__':
    sol = Solution()
    n = 2
    logs = ["0:start:0",
            "1:start:2",
            "1:end:5",
            "0:end:6"]
    print(sol.exclusiveTime(n, logs))
