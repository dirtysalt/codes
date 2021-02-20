class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """

    def precompute_dist(self):
        dist = [0] * 256
        for d in range(0, 256):
            x = min(d // 17, 15)
            if (x + 1) < 16 and abs(x * 17 - d) > abs((x + 1) * 17 - d):
                dist[d] = (x + 1) * 17
            else:
                dist[d] = x * 17
        return dist

    def str2int(self, s):
        res = 0
        for c in s:
            v = 0
            if ord('0') <= ord(c) <= ord('9'):
                v += ord(c) - ord('0')
            else:
                v += ord(c) - ord('a') + 10
            res = res * 16 + v
        return res

    def int2str(self, v, width = 2):
        s = ''
        while v:
            x = v % 16
            c = ''
            if x < 10:
                c = chr(x + ord('0'))
            else:
                c = chr(x -10 + ord('a'))
            s += c
            v = v // 16
        if len(s) < width:
            s += '0' * (width - len(s))
        return s[::-1]

    def similarRGB(self, color):
        # Write your code here
        dist = self.precompute_dist()
        res = '#'
        for i in range(3):
            s = color[2*i+1:2*i+3]
            value = self.str2int(s)
            #print(s, value)
            exp_value = dist[value]
            #print(exp_value)
            c = self.int2str(exp_value)
            res += c
        #print(res)
        return res
