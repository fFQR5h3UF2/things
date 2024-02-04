# Submission for 'Reverse Words in a String III'
# Submission url: https://leetcode.com/submissions/detail/1064056302/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda word: word[::-1], s.split()))
