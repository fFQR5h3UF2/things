# Submission title: Encode and Decode TinyURL
# Submission url  : https://leetcode.com/problems/encode-and-decode-tinyurl/description/
# Submission url  : https://leetcode.com/submissions/detail/1051791289/
# Submission json : {"id":1051791289,"status_display":"Accepted","lang":"python3","question_id":535,"title_slug":"encode-and-decode-tinyurl","code":"class Codec:\n\n    def __init__(self):\n        self.urls = {}\n        self.id = 0\n\n    def encode(self, longUrl: str) -> str:\n        \"\"\"Encodes a URL to a shortened URL.\n        \"\"\"\n        id = self.id\n        self.urls[id] = longUrl\n        self.id += 1\n        return id\n        \n\n    def decode(self, shortUrl: str) -> str:\n        \"\"\"Decodes a shortened URL to its original URL.\n        \"\"\"\n        return self.urls[int(shortUrl)]\n        \n\n# Your Codec object will be instantiated and called as such:\n# codec = Codec()\n# codec.decode(codec.encode(url))","title":"Encode and Decode TinyURL","url":"/submissions/detail/1051791289/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1694956499,"status":10,"runtime":"28 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Codec:

    def __init__(self):
        self.urls = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        id = self.id
        self.urls[id] = longUrl
        self.id += 1
        return id

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.urls[int(shortUrl)]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
