# Submission title: for Design Authentication Manager
# Submission url  : https://leetcode.com/submissions/detail/1050849923/
# Submission json : {"id": 1050849923, "status_display": "Accepted", "lang": "python3", "question_id": 1905, "title_slug": "design-authentication-manager", "code": "class AuthenticationManager:\n\n    def __init__(self, timeToLive: int):\n        self.ttl = timeToLive\n        self.tokens = {}\n\n    def generate(self, tokenId: str, currentTime: int) -> None:\n        self.tokens[tokenId] = currentTime + self.ttl\n\n    def renew(self, tokenId: str, currentTime: int) -> None:\n        if currentTime < self.tokens.get(tokenId, currentTime):\n            self.generate(tokenId, currentTime)\n        else:\n            self.tokens.pop(tokenId, None)\n\n    def countUnexpiredTokens(self, currentTime: int) -> int:\n        count = 0\n        remove_tokens = []\n        for token, expir_time in self.tokens.items():\n            if currentTime < expir_time:\n                count += 1\n            else:\n                remove_tokens.append(token)\n        \n        for token in remove_tokens:\n            self.tokens.pop(token)\n        \n        return count\n\n\n# Your AuthenticationManager object will be instantiated and called as such:\n# obj = AuthenticationManager(timeToLive)\n# obj.generate(tokenId,currentTime)\n# obj.renew(tokenId,currentTime)\n# param_3 = obj.countUnexpiredTokens(currentTime)", "title": "Design Authentication Manager", "url": "/submissions/detail/1050849923/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694868403, "status": 10, "runtime": "189 ms", "is_pending": "Not Pending", "memory": "17.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if currentTime < self.tokens.get(tokenId, currentTime):
            self.generate(tokenId, currentTime)
        else:
            self.tokens.pop(tokenId, None)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        remove_tokens = []
        for token, expir_time in self.tokens.items():
            if currentTime < expir_time:
                count += 1
            else:
                remove_tokens.append(token)

        for token in remove_tokens:
            self.tokens.pop(token)

        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
