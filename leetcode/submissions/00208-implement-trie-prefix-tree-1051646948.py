# Submission title: for Implement Trie (Prefix Tree)
# Submission url  : https://leetcode.com/submissions/detail/1051646948/
# Submission json : {"id": 1051646948, "status_display": "Accepted", "lang": "python3", "question_id": 208, "title_slug": "implement-trie-prefix-tree", "code": "class Node:\n    def __init__(self):\n        self.ch, self.is_word = [None] * 128, False\n\nclass Trie:\n\n    def __init__(self):\n        self.head = Node()\n\n    def insert(self, word: str) -> None:\n        cur_node = self.head\n        for i in range(len(word)):\n            char = ord(word[i])\n            if cur_node.ch[char] is None:\n                cur_node.ch[char] = Node()\n            cur_node = cur_node.ch[char]\n        cur_node.is_word = True\n\n    def search(self, word: str) -> bool:\n        cur_node = self.head\n        for i in range(len(word)):\n            char = ord(word[i])\n            if cur_node.ch[char] is None:\n                return False\n            cur_node = cur_node.ch[char]\n        \n        return cur_node.is_word\n\n    def startsWith(self, prefix: str) -> bool:\n        cur_node = self.head\n        for i in range(len(prefix)):\n            char = ord(prefix[i])\n            if cur_node.ch[char] is None:\n                return False\n            cur_node = cur_node.ch[char]\n        \n        return True\n\n\n# Your Trie object will be instantiated and called as such:\n# obj = Trie()\n# obj.insert(word)\n# param_2 = obj.search(word)\n# param_3 = obj.startsWith(prefix)", "title": "Implement Trie (Prefix Tree)", "url": "/submissions/detail/1051646948/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1694940000, "status": 10, "runtime": "297 ms", "is_pending": "Not Pending", "memory": "60.3 MB", "compare_result": "1111111111111111", "has_notes": true, "flag_type": 1}


class Node:
    def __init__(self):
        self.ch, self.is_word = [None] * 128, False


class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur_node = self.head
        for i in range(len(word)):
            char = ord(word[i])
            if cur_node.ch[char] is None:
                cur_node.ch[char] = Node()
            cur_node = cur_node.ch[char]
        cur_node.is_word = True

    def search(self, word: str) -> bool:
        cur_node = self.head
        for i in range(len(word)):
            char = ord(word[i])
            if cur_node.ch[char] is None:
                return False
            cur_node = cur_node.ch[char]

        return cur_node.is_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.head
        for i in range(len(prefix)):
            char = ord(prefix[i])
            if cur_node.ch[char] is None:
                return False
            cur_node = cur_node.ch[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
