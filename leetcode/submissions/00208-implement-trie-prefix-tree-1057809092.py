# Submission title: for Implement Trie (Prefix Tree)
# Submission url  : https://leetcode.com/submissions/detail/1057809092/
# Submission json : {"id": 1057809092, "status_display": "Accepted", "lang": "python3", "question_id": 208, "title_slug": "implement-trie-prefix-tree", "code": "class Trie:\n\n    def __init__(self):\n        self.root = {}\n\n    def insert(self, word: str) -> None:\n        cur = self.root\n        for char in word:\n            if char not in cur:\n                cur[char] = {}\n            cur = cur[char]\n        \n        cur[\"_is_word\"] = None\n\n    def search(self, word: str) -> bool:\n        cur = self.root\n        for char in word:\n            if char not in cur:\n                return False\n            cur = cur[char]\n        \n        return \"_is_word\" in cur\n\n    def startsWith(self, prefix: str) -> bool:\n        cur = self.root\n        for char in prefix:\n            if char not in cur:\n                return False\n            cur = cur[char]\n            \n        return True\n\n\n# Your Trie object will be instantiated and called as such:\n# obj = Trie()\n# obj.insert(word)\n# param_2 = obj.search(word)\n# param_3 = obj.startsWith(prefix)", "title": "Implement Trie (Prefix Tree)", "url": "/submissions/detail/1057809092/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695549381, "status": 10, "runtime": "105 ms", "is_pending": "Not Pending", "memory": "29.8 MB", "compare_result": "1111111111111111", "has_notes": false, "flag_type": 1}


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]

        cur["_is_word"] = None

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]

        return "_is_word" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
