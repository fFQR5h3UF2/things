# Submission title: Design HashMap
# Submission url  : https://leetcode.com/problems/design-hashmap/description/
# Submission url  : https://leetcode.com/submissions/detail/1066540135/
# Submission json : {"id":1066540135,"status_display":"Accepted","lang":"python3","question_id":817,"title_slug":"design-hashmap","code":"class ListNode:\n    def __init__(self, key, value):\n        self.key = key\n        self.value = value\n        self.next = None\n\nclass MyHashMap:\n\n    def __init__(self):\n        self.size = 1000\n        self.table = [None] * self.size\n\n    def _index(self, key: int) -> int:\n        return key % self.size\n\n    def put(self, key: int, value: int) -> None:\n        idx = self._index(key)\n        if not self.table[idx]:\n            self.table[idx] = ListNode(key, value)\n            return\n        current = self.table[idx]\n        while current:\n            if current.key == key:\n                current.value = value\n                return\n            if not current.next:\n                current.next = ListNode(key, value)\n                return\n            current = current.next\n\n    def get(self, key: int) -> int:\n        idx = self._index(key)\n        current = self.table[idx]\n        while current:\n            if current.key == key:\n                return current.value\n            current = current.next\n        return -1\n\n    def remove(self, key: int) -> None:\n        idx = self._index(key)\n        current = self.table[idx]\n        if not current:\n            return\n        if current.key == key:\n            self.table[idx] = current.next\n            return\n        while current.next:\n            if current.next.key == key:\n                current.next = current.next.next\n                return\n            current = current.next\n\n\n# Your MyHashMap object will be instantiated and called as such:\n# obj = MyHashMap()\n# obj.put(key,value)\n# param_2 = obj.get(key)\n# obj.remove(key)","title":"Design HashMap","url":"/submissions/detail/1066540135/","lang_name":"Python3","time":"4 months","timestamp":1696399200,"status":10,"runtime":"210 ms","is_pending":"Not Pending","memory":"20.1 MB","compare_result":"111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size

    def _index(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._index(key)
        if not self.table[idx]:
            self.table[idx] = ListNode(key, value)
            return
        current = self.table[idx]
        while current:
            if current.key == key:
                current.value = value
                return
            if not current.next:
                current.next = ListNode(key, value)
                return
            current = current.next

    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.table[idx]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.table[idx]
        if not current:
            return
        if current.key == key:
            self.table[idx] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
