# Submission title: Encode and Decode TinyURL
# Submission url  : https://leetcode.com/problems/encode-and-decode-tinyurl/description/"
# Submission url  : https://leetcode.com/submissions/detail/1051790057/"


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
