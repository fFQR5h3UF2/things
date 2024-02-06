# Submission title: for H-Index
# Submission url  : https://leetcode.com/submissions/detail/998371186/
# Submission json : {"id": 998371186, "status_display": "Accepted", "lang": "python3", "question_id": 274, "title_slug": "h-index", "code": "class Solution:\n    # [3,0,6,1,5]\n    # [0,1,3,5,6]\n    def hIndex(self, citations: List[int]) -> int:\n        citations = sorted(citations)\n        length = len(citations)\n\n        h = 0\n        for i in reversed(range(length)):\n            citations_count = citations[i]\n            published_count = length - i\n\n            if citations_count == 0 or published_count < h:\n                break\n\n            if published_count <= citations_count:\n                h = published_count\n            \n        return h\n\n", "title": "H-Index", "url": "/submissions/detail/998371186/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689763171, "status": 10, "runtime": "61 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # [3,0,6,1,5]
    # [0,1,3,5,6]
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        length = len(citations)

        h = 0
        for i in reversed(range(length)):
            citations_count = citations[i]
            published_count = length - i

            if citations_count == 0 or published_count < h:
                break

            if published_count <= citations_count:
                h = published_count

        return h
