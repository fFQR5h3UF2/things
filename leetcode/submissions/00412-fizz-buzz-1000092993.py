# Submission title: for Fizz Buzz
# Submission url  : https://leetcode.com/submissions/detail/1000092993/
# Submission json : {"id": 1000092993, "status_display": "Accepted", "lang": "python3", "question_id": 412, "title_slug": "fizz-buzz", "code": "class Solution:\n    def fizzBuzz(self, n: int) -> List[str]:\n        result = []\n\n        for i in range(1, n + 1):\n            div_by_3, div_by_5 = i % 3 == 0, i % 5 == 0\n            value = None\n\n            if div_by_3 and div_by_5:\n                value = \"FizzBuzz\"\n            elif div_by_3:\n                value = \"Fizz\"\n            elif div_by_5:\n                value = \"Buzz\"\n            else:\n                value = str(i)\n            \n            result.append(value)\n        \n        return result", "title": "Fizz Buzz", "url": "/submissions/detail/1000092993/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689935581, "status": 10, "runtime": "52 ms", "is_pending": "Not Pending", "memory": "17.4 MB", "compare_result": "11111111", "has_notes": false, "flag_type": 1}


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            div_by_3, div_by_5 = i % 3 == 0, i % 5 == 0
            value = None

            if div_by_3 and div_by_5:
                value = "FizzBuzz"
            elif div_by_3:
                value = "Fizz"
            elif div_by_5:
                value = "Buzz"
            else:
                value = str(i)

            result.append(value)

        return result
