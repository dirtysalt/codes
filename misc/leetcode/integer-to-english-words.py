#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        pws = [
            (10 ** 9, "Billion"),
            (10 ** 6, "Million"),
            (10 ** 3, "Thousand"),
            (10 ** 2, "Hundred")
        ]

        words = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]

        words2 = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def speak(num):
            res = []
            if (num < 20):
                res.append(words[num])
            elif (num < 100):
                res.append(words2[num // 10])
                res.append(words[num % 10])
            else:
                for (pw, name) in pws:
                    if (num >= pw):
                        res.extend(speak(num // pw))
                        res.append(name)
                        num %= pw
                res.extend(speak(num))
            return res

        res = [x for x in speak(num) if x]
        return ' '.join(res)


if __name__ == '__main__':
    s = Solution()
    for n in (1, 12, 123, 12345, 123456, 1234567, 12345678, 123456789):
        print((s.numberToWords(n)))
