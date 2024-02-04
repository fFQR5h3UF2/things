# Submission for LRU Cache
# Submission url: https://leetcode.com/submissions/detail/997696599/


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
        self.delete_node(result_node)
        self.add_node(result_node)
        return result_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            current = self.cache[key]
            del self.cache[key]
            self.delete_node(current)

        if len(self.cache) == self.cap:
            last = self.tail.prev
            del self.cache[last.prev.key]
            self.delete_node(last.prev)

        new_node = self.Node(key, value)
        self.add_node(new_node)
        self.cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
