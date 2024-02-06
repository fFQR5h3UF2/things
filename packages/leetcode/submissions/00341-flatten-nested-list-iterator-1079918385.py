# Submission title: for Flatten Nested List Iterator
# Submission url  : https://leetcode.com/submissions/detail/1079918385/
# Submission json : {"id": 1079918385, "status_display": "Accepted", "lang": "python3", "question_id": 341, "title_slug": "flatten-nested-list-iterator", "code": "# \"\"\"\n# This is the interface that allows for creating nested lists.\n# You should not implement it, or speculate about its implementation\n# \"\"\"\n#class NestedInteger:\n#    def isInteger(self) -> bool:\n#        \"\"\"\n#        @return True if this NestedInteger holds a single integer, rather than a nested list.\n#        \"\"\"\n#\n#    def getInteger(self) -> int:\n#        \"\"\"\n#        @return the single integer that this NestedInteger holds, if it holds a single integer\n#        Return None if this NestedInteger holds a nested list\n#        \"\"\"\n#\n#    def getList(self) -> [NestedInteger]:\n#        \"\"\"\n#        @return the nested list that this NestedInteger holds, if it holds a nested list\n#        Return None if this NestedInteger holds a single integer\n#        \"\"\"\n\nclass NestedIterator:\n    def __init__(self, nestedList: [NestedInteger]):\n        self.list = []\n        self.flatten(self.list, nestedList)\n        self.cur = 0\n        self.length = len(self.list)\n\n    def flatten(self, flatList: List[int], nestedList: List[NestedInteger]):\n        for ni in nestedList:\n            if ni.isInteger():\n                flatList.append(ni.getInteger())\n            else:\n                self.flatten(flatList, ni.getList())\n\n    def next(self) -> int: \n        answer = self.list[self.cur]\n        self.cur += 1\n        return answer\n    \n    def hasNext(self) -> bool:\n        return self.cur < self.length\n\n# Your NestedIterator object will be instantiated and called as such:\n# i, v = NestedIterator(nestedList), []\n# while i.hasNext(): v.append(i.next())", "title": "Flatten Nested List Iterator", "url": "/submissions/detail/1079918385/", "lang_name": "Python3", "time": "3\u00a0months, 2\u00a0weeks", "timestamp": 1697807196, "status": 10, "runtime": "51 ms", "is_pending": "Not Pending", "memory": "19.9 MB", "compare_result": "1111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.flatten(self.list, nestedList)
        self.cur = 0
        self.length = len(self.list)

    def flatten(self, flatList: List[int], nestedList: List[NestedInteger]):
        for ni in nestedList:
            if ni.isInteger():
                flatList.append(ni.getInteger())
            else:
                self.flatten(flatList, ni.getList())

    def next(self) -> int:
        answer = self.list[self.cur]
        self.cur += 1
        return answer

    def hasNext(self) -> bool:
        return self.cur < self.length


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
