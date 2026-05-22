class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        n = len(words)
        m = len(words[0])
        max_k = min(n, m)
        for k in range(max_k):
            for c in range(max_k):
                if words[k][c] != words[c][k]:
                    return False
        return True
