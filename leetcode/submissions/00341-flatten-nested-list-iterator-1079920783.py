# Submission title: Flatten Nested List Iterator
# Submission url  : https://leetcode.com/problems/flatten-nested-list-iterator/description/
# Submission url  : https://leetcode.com/submissions/detail/1079920783/
# Submission json : {"id":1079920783,"status_display":"Accepted","lang":"python3","question_id":341,"title_slug":"flatten-nested-list-iterator","code":"# \"\"\"\n# This is the interface that allows for creating nested lists.\n# You should not implement it, or speculate about its implementation\n# \"\"\"\n#class NestedInteger:\n#    def isInteger(self) -> bool:\n#        \"\"\"\n#        @return True if this NestedInteger holds a single integer, rather than a nested list.\n#        \"\"\"\n#\n#    def getInteger(self) -> int:\n#        \"\"\"\n#        @return the single integer that this NestedInteger holds, if it holds a single integer\n#        Return None if this NestedInteger holds a nested list\n#        \"\"\"\n#\n#    def getList(self) -> [NestedInteger]:\n#        \"\"\"\n#        @return the nested list that this NestedInteger holds, if it holds a nested list\n#        Return None if this NestedInteger holds a single integer\n#        \"\"\"\n\nclass NestedIterator:\n    def __init__(self, nestedList: [NestedInteger]):\n        self.get_next = self.get_next_gen(nestedList)\n        self.next_val = next(self.get_next, None)\n\n    def get_next_gen(self, nestedList: List[NestedInteger]) -> Generator[None, None, int]:\n        for ni in nestedList:\n            if ni.isInteger():\n                yield ni.getInteger()\n            else:\n                yield from self.get_next_gen(ni.getList())\n\n    def next(self) -> int: \n        answer, self.next_val = self.next_val, next(self.get_next, None)\n        return answer\n    \n    def hasNext(self) -> bool:\n        return self.next_val is not None\n\n# Your NestedIterator object will be instantiated and called as such:\n# i, v = NestedIterator(nestedList), []\n# while i.hasNext(): v.append(i.next())","title":"Flatten Nested List Iterator","url":"/submissions/detail/1079920783/","lang_name":"Python3","time":"3 months, 2 weeks","timestamp":1697807498,"status":10,"runtime":"59 ms","is_pending":"Not Pending","memory":"19.8 MB","compare_result":"1111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

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
        self.get_next = self.get_next_gen(nestedList)
        self.next_val = next(self.get_next, None)

    def get_next_gen(
        self, nestedList: List[NestedInteger]
    ) -> Generator[None, None, int]:
        for ni in nestedList:
            if ni.isInteger():
                yield ni.getInteger()
            else:
                yield from self.get_next_gen(ni.getList())

    def next(self) -> int:
        answer, self.next_val = self.next_val, next(self.get_next, None)
        return answer

    def hasNext(self) -> bool:
        return self.next_val is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
