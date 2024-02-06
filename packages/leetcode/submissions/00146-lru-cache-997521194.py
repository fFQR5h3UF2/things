# Submission title: for LRU Cache
# Submission url  : https://leetcode.com/submissions/detail/997521194/
# Submission json : {"id": 997521194, "status_display": "Accepted", "lang": "python3", "question_id": 146, "title_slug": "lru-cache", "code": "class LRUCache:\n    class Node:\n        def __init__(self, key: str, val: int) -> None:\n            self.key = key\n            self.val = val\n            self.prev: Node = None\n            self.next: Node = None\n\n    def __init__(self, capacity: int) -> None:\n        self.cap = capacity\n        self.head = self.Node(-1, -1)\n        self.tail = self.Node(-1, -1)\n        self.head.next = self.tail\n        self.tail.prev = self.head\n        self.cache = {}\n\n    def add_node(self, new_node: Node) -> None:\n        old_first_node = self.head.next\n        new_node.next = old_first_node\n        new_node.prev = self.head\n        self.head.next = new_node\n        old_first_node.prev = new_node\n\n    def delete_node(self, delete_node: Node) -> None:\n        prev = delete_node.prev\n        next = delete_node.next\n        prev.next = next\n        next.prev = prev\n\n    def get(self, key: int) -> int:\n        if key not in self.cache:\n            return -1\n        result_node = self.cache[key]\n        result = result_node.val\n        del self.cache[key]\n        self.delete_node(result_node)\n        self.add_node(result_node)\n        self.cache[key] = self.head.next\n        return result\n    \n\n    def put(self, key: int, value: int) -> None:\n        if key in self.cache:\n            current = self.cache[key]\n            del self.cache[key]\n            self.delete_node(current)\n\n        if len(self.cache) == self.cap:\n            del self.cache[self.tail.prev.key]\n            self.delete_node(self.tail.prev)\n\n        self.add_node(self.Node(key, value))\n        self.cache[key] = self.head.next\n\n# Your LRUCache object will be instantiated and called as such:\n# obj = LRUCache(capacity)\n# param_1 = obj.get(key)\n# obj.put(key,value)", "title": "LRU Cache", "url": "/submissions/detail/997521194/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689680797, "status": 10, "runtime": "857 ms", "is_pending": "Not Pending", "memory": "77.8 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class LRUCache:
    class Node:
        def __init__(self, key: str, val: int) -> None:
            self.key = key
            self.val = val
            self.prev: Node = None
            self.next: Node = None

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def add_node(self, new_node: Node) -> None:
        old_first_node = self.head.next
        new_node.next = old_first_node
        new_node.prev = self.head
        self.head.next = new_node
        old_first_node.prev = new_node

    def delete_node(self, delete_node: Node) -> None:
        prev = delete_node.prev
        next = delete_node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        result_node = self.cache[key]
        result = result_node.val
        del self.cache[key]
        self.delete_node(result_node)
        self.add_node(result_node)
        self.cache[key] = self.head.next
        return result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            current = self.cache[key]
            del self.cache[key]
            self.delete_node(current)

        if len(self.cache) == self.cap:
            del self.cache[self.tail.prev.key]
            self.delete_node(self.tail.prev)

        self.add_node(self.Node(key, value))
        self.cache[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
