# Submission title: for Prime Number of Set Bits in Binary Representation
# Submission url  : https://leetcode.com/submissions/detail/1056027873/
# Submission json : {"id": 1056027873, "status_display": "Accepted", "lang": "python3", "question_id": 767, "title_slug": "prime-number-of-set-bits-in-binary-representation", "code": "class Solution:\n    def countPrimeSetBits(self, left: int, right: int) -> int:\n        prime_bits = (2, 3, 5, 7, 11, 13, 17, 19)\n        answer = 0\n        for num in range(left, right + 1):\n            bit_count = num.bit_count()\n            if bit_count in prime_bits:\n                answer += 1\n            \n        return answer", "title": "Prime Number of Set Bits in Binary Representation", "url": "/submissions/detail/1056027873/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695361885, "status": 10, "runtime": "85 ms", "is_pending": "Not Pending", "memory": "16 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_bits = (2, 3, 5, 7, 11, 13, 17, 19)
        answer = 0
        for num in range(left, right + 1):
            bit_count = num.bit_count()
            if bit_count in prime_bits:
                answer += 1

        return answer
