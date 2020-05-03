class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        # write your code here
        st = []
        total = 0
        p = 0
        max_length = 0
        # print(len(input))
        while p < len(input):
            depth = 0
            while p < len(input) and input[p] == "\t":
                depth += 1
                p += 1
            while depth < len(st):
                total -= st[-1]
                st.pop(-1)

            s, e = p, p
            is_file = False
            while e < len(input) and input[e] != "\n":
                if input[e] == '.':
                    is_file = True
                e += 1

            length = (e - s)
            # print(length, is_file)
            if is_file:
                if (length + total) > max_length:
                    max_length = length + total
            else:
                st.append(length + 1) # '\n as /'
                total += length + 1
            p = e + 1
        return max_length
