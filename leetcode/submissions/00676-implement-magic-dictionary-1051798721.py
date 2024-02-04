# Submission title: for Implement Magic Dictionary
# Submission url  : https://leetcode.com/submissions/detail/1051798721/
# Submission json : {"id": 1051798721, "status_display": "Accepted", "lang": "python3", "question_id": 676, "title_slug": "implement-magic-dictionary", "code": "class MagicDictionary:\n\n    def __init__(self):\n        self.dict = []\n\n    def buildDict(self, dictionary: List[str]) -> None:\n        self.dict = dictionary\n\n    def search(self, searchWord: str) -> bool:\n        target_length = len(searchWord)\n        for word in self.dict:\n            if len(word) != target_length or word == searchWord:\n                continue\n            found_diff = False\n            for i in range(target_length):\n                if word[i] == searchWord[i]:\n                    continue\n                if found_diff:\n                    break\n\n                found_diff = True\n            else:\n                return True\n\n        return False\n\n# Your MagicDictionary object will be instantiated and called as such:\n# obj = MagicDictionary()\n# obj.buildDict(dictionary)\n# param_2 = obj.search(searchWord)", "title": "Implement Magic Dictionary", "url": "/submissions/detail/1051798721/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1694957224, "status": 10, "runtime": "66 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class MagicDictionary:

    def __init__(self):
        self.dict = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.dict = dictionary

    def search(self, searchWord: str) -> bool:
        target_length = len(searchWord)
        for word in self.dict:
            if len(word) != target_length or word == searchWord:
                continue
            found_diff = False
            for i in range(target_length):
                if word[i] == searchWord[i]:
                    continue
                if found_diff:
                    break

                found_diff = True
            else:
                return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
