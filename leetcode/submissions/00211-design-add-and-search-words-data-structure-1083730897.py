# Submission title: Design Add and Search Words Data Structure
# Submission url  : https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# Submission url  : https://leetcode.com/submissions/detail/1083730897/
# Submission json : {"id":1083730897,"status_display":"Accepted","lang":"python3","question_id":211,"title_slug":"design-add-and-search-words-data-structure","code":"class TrieNode:\n    def __init__(self):\n        self.children = {}\n        self.is_word = False\n\nclass WordDictionary:\n\n    def __init__(self):\n        self.root = TrieNode()\n\n    def addWord(self, word: str) -> None:\n        cur = self.root\n        for char in word:\n            cur = cur.children.setdefault(char, TrieNode())\n        cur.is_word = True\n\n    def search(self, word: str) -> bool:\n        cur, nxt = [self.root], []\n        \n        for char in word:\n            if not cur:\n                return False\n\n            if char == \".\":\n                for node in cur:\n                    nxt.extend(node.children.values())\n            else:\n                for node in cur:\n                    if char in node.children:\n                        nxt.append(node.children[char]) \n                \n            cur.clear()\n            cur, nxt = nxt, cur\n\n        return any(node.is_word for node in cur)\n            \n\n\n\n# Your WordDictionary object will be instantiated and called as such:\n# obj = WordDictionary()\n# obj.addWord(word)\n# param_2 = obj.search(word)","title":"Design Add and Search Words Data Structure","url":"/submissions/detail/1083730897/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698230259,"status":10,"runtime":"2418 ms","is_pending":"Not Pending","memory":"80.1 MB","compare_result":"11111111111111111111111111111","has_notes":false,"flag_type":1}


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children.setdefault(char, TrieNode())
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur, nxt = [self.root], []

        for char in word:
            if not cur:
                return False

            if char == ".":
                for node in cur:
                    nxt.extend(node.children.values())
            else:
                for node in cur:
                    if char in node.children:
                        nxt.append(node.children[char])

            cur.clear()
            cur, nxt = nxt, cur

        return any(node.is_word for node in cur)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
