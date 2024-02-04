# Submission title: for Maximize the Confusion of an Exam
# Submission url  : https://leetcode.com/submissions/detail/1010336801/
# Submission json : {"id": 1010336801, "status_display": "Accepted", "lang": "python3", "question_id": 2134, "title_slug": "maximize-the-confusion-of-an-exam", "code": "class Solution:\n    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:\n        length = len(answerKey)\n        char_t, char_f = \"T\", \"F\"\n        max_size = k\n        count = defaultdict(int)\n        \n        for char in answerKey[:k]:\n            count[char] += 1\n\n        left = 0\n        for right in range(k, length):\n            count[answerKey[right]] += 1\n            \n            while min(count[char_t], count[char_f]) > k: \n                count[answerKey[left]] -= 1\n                left += 1\n            \n            size = right - left + 1\n            if size > max_size:\n                max_size = size\n                    \n        return max_size\n\n\n\n        \n", "title": "Maximize the Confusion of an Exam", "url": "/submissions/detail/1010336801/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1690986804, "status": 10, "runtime": "239 ms", "is_pending": "Not Pending", "memory": "16.8 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        length = len(answerKey)
        char_t, char_f = "T", "F"
        max_size = k
        count = defaultdict(int)

        for char in answerKey[:k]:
            count[char] += 1

        left = 0
        for right in range(k, length):
            count[answerKey[right]] += 1

            while min(count[char_t], count[char_f]) > k:
                count[answerKey[left]] -= 1
                left += 1

            size = right - left + 1
            if size > max_size:
                max_size = size

        return max_size
