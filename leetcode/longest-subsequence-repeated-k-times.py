#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter
        cnt = Counter(s)

        buf = []
        for c in range(26):
            c2 = chr(ord('a') + c)
            cnt[c2] //= k
            if cnt[c2] > 0:
                buf.extend([c2] * cnt[c2])

        # get permutation in reverse lex order.
        buf.sort(reverse=True)

        s = ''.join([x for x in s if cnt[x]])
        if not s: return ''

        def ok(tmp):
            rep = k * len(tmp)
            j = 0
            for c in s:
                if tmp[j] == c:
                    rep -= 1
                    if rep == 0:
                        return True
                    j = (j + 1) % len(tmp)
            return False

        m = len(buf)
        for sz in reversed(range(1, m + 1)):
            import itertools
            for w in itertools.permutations(buf, sz):
                if ok(w):
                    return ''.join(w)
        return ''


true, false, null = True, False, None
cases = [
    ("letsleetcode", 2, "let"),
    ("bb", 2, "b"),
    ("ab", 2, ""),
    ("bbabbabbbbabaababab", 3, "bbbb"),
    ("tdpvgkahikgkkgkkkegwkkzgkkgkk", 6, "gkk"),
    ("coqdndqojcqxndojcqndojrcqndojcqndojcqndnojcqzndojcqndojcqnudojcqndvojcqndoj", 11, "cqndoj"),
    (
        "ororobrorororororhororosrorordorowrororororsororyororororororosrorororojjrorororororoprorvorxorororororoqrhoriorozrorcorzororkororokrororornorororororortorosroyrohrorwhorovrorxoro",
        74, "ro"),
    (
        "qqvekmkqvyekmkqvekgmkqvekmkqfvekmkqvekmkqvzekmkqvekmkrqvekrmkqvekmakqvetkmkqvvekhmkqvekamkqvekmkqmvuekmkqvekmkqvekbmkqveykmykqveklemkqvekmkqvekmkqvekmkqvekmkqvekmkqvekmkqvekmkqvrekmkqvekemfkgqvekmkqvekcnmkqvekmkqvekmkqvceikmkqqvekmkqvaekmkqvekmkqvekmkqvnevkjnmkqveifkmakqvekmkqvekmkqupvhzekmkqviekbmkqvekmkqvxekrmkqvekmkqvekmkqveckmkqvtekmkqvekmikqvekmkqvekmkqvekmkvqcvekmkqvekmkvqvekmktqvekmkqvcekmkqvebkmkjqvekmkqvekmkqvekmkqwvekmkqvekmfkqvekmkqvekcmkcqveqkmkqvyekhmkqvekmkqxvekgdmjkqvekmtkqvekmkqvhekmmkxqveikmbkqvekmkqvekmkqvekmkbqvekmkqvekmlkqvzekmkqvaiyekmkqvuekmkqvorekjmkqverkmkqvekmrkqveklmksqnvekmkwqvekmkqvedkmkqvekmgkqxvekmkqvekmfkqvhekmnkqvehckmkqvekmkqvekmkqvekmkyqvektmkqvekmkqvekmkqvekmkqvekmkqvekmkqvekpgsmkqdvekmkqveknmkqveakmkqvekmkqvekzmkqvekmkqvkekmk",
        111,
        "qvekmk"),
    (
        "sctorqfpfstorqpstorqpstorqpstorqpystorqpstorqpstourqpustorqpstorqpstorqpstorqpsetlobrqpstorqppstorqpstorqzbpdstorqpstqowrqpstorlqpstworqpstorqpstorqpstorqpsvdtorqpstgorqpstorqpstorqpstorqnpstorqpstorqpsftoruqpstorqpstorrqpsyctorqpustocrqpstorqpstqorqrpstmorqpdstorqpstorqpstordqpshtjorqpstorqpstorqpstorqpsqtorxqpsctorpqmpstorqpstorqpstolrqpstorqpbstoerbqpstorqpstorqpstoarqpstorqpstorqpstorqapstorqpsytorqpstorqpstorqpstoreqpstothrxqepstorqpezstpqorqpstorqpstorqpstorqpstorqxpfstorqpstorqpstorqpstnorocqpstorqpstojrqppstorghqhpstorqnpstorqbpstohtrqpstorqpstorqpstorqpnstotrqprsdtorqpstuvourqpsftoorqpstonrqlbpstgjorqpsxtorqpstorobqpsctorqpstorqpstorqpstoarqpstorqpstorqpsltorvqpstorqpostotrqpstorqptstorqmpstocrtqpstiorwqpznvstoriqpstorbqpstorqpstonrqpstorqpsqtorqepstorqpustorqpsttorqpd",
        113, "storqp")
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestSubsequenceRepeatedK, cases)

if __name__ == '__main__':
    pass
