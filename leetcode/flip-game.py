class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        res = []
        n = len(s)
        for i in range(1, n):
            if s[i-1:i+1] == '++':
                s2 = s[:i-1] + '--' + s[i+1:]
                res.append(''.join(s2))
        return res
