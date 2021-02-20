# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.items = []
        self.st = []
        self.st.append((0, nestedList))
        while self.st:
            (idx, nsl) = self.st[-1]
            self.st.pop()
            while idx < len(nsl):
                element = nsl[idx]
                idx += 1
                if element.isInteger():
                    self.items.append(element)
                    continue
                else:
                    self.st.append((idx, nsl))
                    self.st.append((0, element.getList()))
                    break
        self.it = 0

    def next(self):
        element = self.items[self.it]
        self.it += 1
        return element.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.it != len(self.items)


if __name__ == '__main__':
    # Your NestedIterator object will be instantiated and called as such:
    # i, v = NestedIterator(nestedList), []
    # while i.hasNext(): v.append(i.next())
    pass
