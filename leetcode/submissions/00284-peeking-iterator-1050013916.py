# Submission title: for Peeking Iterator
# Submission url  : https://leetcode.com/submissions/detail/1050013916/
# Submission json : {"id": 1050013916, "status_display": "Accepted", "lang": "python3", "question_id": 284, "title_slug": "peeking-iterator", "code": "# Below is the interface for Iterator, which is already defined for you.\n#\n# class Iterator:\n#     def __init__(self, nums):\n#         \"\"\"\n#         Initializes an iterator object to the beginning of a list.\n#         :type nums: List[int]\n#         \"\"\"\n#\n#     def hasNext(self):\n#         \"\"\"\n#         Returns true if the iteration has more elements.\n#         :rtype: bool\n#         \"\"\"\n#\n#     def next(self):\n#         \"\"\"\n#         Returns the next element in the iteration.\n#         :rtype: int\n#         \"\"\"\n\nclass PeekingIterator:\n    def __init__(self, iterator):\n        \"\"\"\n        Initialize your data structure here.\n        :type iterator: Iterator\n        \"\"\"\n        self._iter = iterator\n        self._next = iterator.next()\n        \n\n    def peek(self):\n        \"\"\"\n        Returns the next element in the iteration without advancing the iterator.\n        :rtype: int\n        \"\"\"\n        return self._next\n        \n\n    def next(self):\n        \"\"\"\n        :rtype: int\n        \"\"\"\n        cur_next = self._next\n        self._next = self._iter.next() if self._iter.hasNext() else None\n        return cur_next\n        \n\n    def hasNext(self):\n        \"\"\"\n        :rtype: bool\n        \"\"\"\n        return self._next is not None\n        \n\n# Your PeekingIterator object will be instantiated and called as such:\n# iter = PeekingIterator(Iterator(nums))\n# while iter.hasNext():\n#     val = iter.peek()   # Get the next element but not advance the iterator.\n#     iter.next()         # Should return the same value as [val].", "title": "Peeking Iterator", "url": "/submissions/detail/1050013916/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694771470, "status": 10, "runtime": "39 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111", "has_notes": false, "flag_type": 1}


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iter = iterator
        self._next = iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        cur_next = self._next
        self._next = self._iter.next() if self._iter.hasNext() else None
        return cur_next

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
