# Submission title: Minimum Deletions to Make Character Frequencies Unique
# Submission url  : https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/
# Submission url  : https://leetcode.com/submissions/detail/1047265181/
# Submission json : {"id":1047265181,"status_display":"Accepted","lang":"python3","question_id":1770,"title_slug":"minimum-deletions-to-make-character-frequencies-unique","code":"class Solution:\n    def minDeletions(self, s: str) -> int:\n        length = len(s)\n        char_count = Counter(s)\n        counts = set()\n        deleted_chars = 0\n\n        for char, count in char_count.items():\n            while count != 0 and count in counts:\n                count -= 1\n                deleted_chars += 1\n            if count != 0:\n                counts.add(count)\n            \n        return deleted_chars\n","title":"Minimum Deletions to Make Character Frequencies Unique","url":"/submissions/detail/1047265181/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694505304,"status":10,"runtime":"111 ms","is_pending":"Not Pending","memory":"17.2 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minDeletions(self, s: str) -> int:
        length = len(s)
        char_count = Counter(s)
        counts = set()
        deleted_chars = 0

        for char, count in char_count.items():
            while count != 0 and count in counts:
                count -= 1
                deleted_chars += 1
            if count != 0:
                counts.add(count)

        return deleted_chars
