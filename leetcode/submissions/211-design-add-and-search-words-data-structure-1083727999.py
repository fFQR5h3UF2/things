# Submission for Design Add and Search Words Data Structure
# Submission url: https://leetcode.com/submissions/detail/1083727999/


class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        cur = self.words
        for char in word:
            cur[char] = {}
            cur = cur[char]
        cur["_is_word"] = True

    def search(self, word: str) -> bool:
        cur, nxt = [self.words], []

        for char in word:
            if not cur:
                return False

            if char == ".":
                for chars in cur:
                    nxt.extend(chars.values())
            else:
                for chars in cur:
                    if char in chars:
                        nxt.append(chars[char])

            cur.clear()
            cur, nxt = nxt, cur

        for chars in cur:
            if "_is_word" in chars:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
