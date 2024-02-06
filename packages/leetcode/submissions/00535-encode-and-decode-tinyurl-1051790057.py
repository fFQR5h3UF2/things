# Submission title: for Encode and Decode TinyURL
# Submission url  : https://leetcode.com/submissions/detail/1051790057/
# Submission json : {"id": 1051790057, "status_display": "Accepted", "lang": "python3", "question_id": 535, "title_slug": "encode-and-decode-tinyurl", "code": "class Codec:\n\n    def __init__(self):\n        self.urls = []\n\n    def encode(self, longUrl: str) -> str:\n        \"\"\"Encodes a URL to a shortened URL.\n        \"\"\"\n        self.urls.append(longUrl)\n        return str(len(self.urls) - 1)\n        \n\n    def decode(self, shortUrl: str) -> str:\n        \"\"\"Decodes a shortened URL to its original URL.\n        \"\"\"\n        return self.urls[int(shortUrl)]\n        \n\n# Your Codec object will be instantiated and called as such:\n# codec = Codec()\n# codec.decode(codec.encode(url))", "title": "Encode and Decode TinyURL", "url": "/submissions/detail/1051790057/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1694956372, "status": 10, "runtime": "42 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Codec:

    def __init__(self):
        self.urls = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.urls.append(longUrl)
        return str(len(self.urls) - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.urls[int(shortUrl)]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
