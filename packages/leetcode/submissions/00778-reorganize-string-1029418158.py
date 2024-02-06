# Submission title: for Reorganize String
# Submission url  : https://leetcode.com/submissions/detail/1029418158/
# Submission json : {"id": 1029418158, "status_display": "Accepted", "lang": "python3", "question_id": 778, "title_slug": "reorganize-string", "code": "class Solution:\n    def reorganizeString(self, s: str) -> str:\n        result = []\n        # Min heap ordered by character counts, so we will use\n        # negative values for count\n        priority_queue = [(-count, char) for char, count in Counter(s).items()]\n        heapify(priority_queue)\n\n        while priority_queue:\n            count_first, char_first = heappop(priority_queue)\n            if not result or char_first != result[-1]:\n                result.append(char_first)\n                if count_first != -1: \n                    heappush(priority_queue, (count_first + 1, char_first))\n                continue\n            \n            if not priority_queue: \n                return \"\"\n            \n            count_second, char_second = heappop(priority_queue)\n            result.append(char_second)\n            if count_second != -1:\n                heappush(priority_queue, (count_second + 1, char_second))\n            heappush(priority_queue, (count_first, char_first))\n\n        return \"\".join(result)", "title": "Reorganize String", "url": "/submissions/detail/1029418158/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692783904, "status": 10, "runtime": "45 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def reorganizeString(self, s: str) -> str:
        result = []
        # Min heap ordered by character counts, so we will use
        # negative values for count
        priority_queue = [(-count, char) for char, count in Counter(s).items()]
        heapify(priority_queue)

        while priority_queue:
            count_first, char_first = heappop(priority_queue)
            if not result or char_first != result[-1]:
                result.append(char_first)
                if count_first != -1:
                    heappush(priority_queue, (count_first + 1, char_first))
                continue

            if not priority_queue:
                return ""

            count_second, char_second = heappop(priority_queue)
            result.append(char_second)
            if count_second != -1:
                heappush(priority_queue, (count_second + 1, char_second))
            heappush(priority_queue, (count_first, char_first))

        return "".join(result)
