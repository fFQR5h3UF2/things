# Submission title: for 3Sum
# Submission url  : https://leetcode.com/submissions/detail/1018504399/
# Submission json : {"id": 1018504399, "status_display": "Accepted", "lang": "python3", "question_id": 15, "title_slug": "3sum", "code": "class Solution:\n    def threeSum(self, nums: List[int]) -> List[List[int]]:\n        result = set()\n\n        #1. Split nums into three lists: negative numbers, positive numbers, and zeros\n        negatives, positives, zeros = [], [], []\n        for num in nums:\n            if num > 0:\n                positives.append(num)\n            elif num < 0: \n                negatives.append(num)\n            else:\n                zeros.append(num)\n\n        #2. Create a separate set for negatives and positives for O(1) look-up times\n        negatives_count, positives_count, zeros_count = len(negatives), len(positives), len(zeros)\n        negatives_set, positives_set = set(negatives), set(positives)\n\n        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P\n        #   i.e. (-3, 0, 3) = 0\n        for num in positives_set if zeros else []:\n            negative = -1 * num\n            if negative in negatives_set:\n                result.add((negative, 0, num))\n\n        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0\n        if zeros_count >= 3:\n            result.add((0, 0, 0))\n\n        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)\n        #   exists in the positive number set\n        for i in range(negatives_count):\n            negative_1 = negatives[i]\n            for j in range(i + 1, negatives_count):\n                negative_2 = negatives[j]\n                target = -1 * (negative_1 + negative_2)\n                if target in positives_set:\n                    result.add(tuple(sorted([negative_1, negative_2, target])))\n\n        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)\n        #   exists in the negative number set\n        for i in range(positives_count):\n            positive_1 = positives[i]\n            for j in range(i + 1, positives_count):\n                positive_2 = positives[j]\n                target = -1 * (positive_1 + positive_2)\n                if target in negatives_set:\n                    result.add(tuple(sorted([positive_1, positive_2, target])))\n\n        return result", "title": "3Sum", "url": "/submissions/detail/1018504399/", "lang_name": "Python3", "time": "5\u00a0months, 3\u00a0weeks", "timestamp": 1691765526, "status": 10, "runtime": "602 ms", "is_pending": "Not Pending", "memory": "20.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        negatives, positives, zeros = [], [], []
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeros.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        negatives_count, positives_count, zeros_count = (
            len(negatives),
            len(positives),
            len(zeros),
        )
        negatives_set, positives_set = set(negatives), set(positives)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        for num in positives_set if zeros else []:
            negative = -1 * num
            if negative in negatives_set:
                result.add((negative, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if zeros_count >= 3:
            result.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(negatives_count):
            negative_1 = negatives[i]
            for j in range(i + 1, negatives_count):
                negative_2 = negatives[j]
                target = -1 * (negative_1 + negative_2)
                if target in positives_set:
                    result.add(tuple(sorted([negative_1, negative_2, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(positives_count):
            positive_1 = positives[i]
            for j in range(i + 1, positives_count):
                positive_2 = positives[j]
                target = -1 * (positive_1 + positive_2)
                if target in negatives_set:
                    result.add(tuple(sorted([positive_1, positive_2, target])))

        return result
