# Submission title: Combinations
# Submission url  : https://leetcode.com/problems/combinations/description/
# Submission url  : https://leetcode.com/submissions/detail/1009431912/
# Submission json : {"id":1009431912,"status_display":"Accepted","lang":"python3","question_id":77,"title_slug":"combinations","code":"class Solution:\n    def combine(self, n: int, k: int) -> List[List[int]]:\n        def generate_combinations(elems: List[int], num: int):\n            total = len(elems)\n            if num > total:\n                return\n            curr_indices = list(range(num))\n            reversed_num = tuple(reversed(range(num)))\n\n            while True:\n                yield list(elems[i] for i in curr_indices)\n                \n                for idx in reversed_num:\n                    if curr_indices[idx] != idx + total - num:\n                        break\n                else:\n                    return\n\n                curr_indices[idx] += 1\n                for j in range(idx+1, num):\n                    curr_indices[j] = curr_indices[j-1] + 1\n\n        return [combination for combination in generate_combinations(tuple(range(1, n+1)), k)]","title":"Combinations","url":"/submissions/detail/1009431912/","lang_name":"Python3","time":"6 months, 1 week","timestamp":1690899295,"status":10,"runtime":"82 ms","is_pending":"Not Pending","memory":"18.1 MB","compare_result":"111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate_combinations(elems: List[int], num: int):
            total = len(elems)
            if num > total:
                return
            curr_indices = list(range(num))
            reversed_num = tuple(reversed(range(num)))

            while True:
                yield list(elems[i] for i in curr_indices)

                for idx in reversed_num:
                    if curr_indices[idx] != idx + total - num:
                        break
                else:
                    return

                curr_indices[idx] += 1
                for j in range(idx + 1, num):
                    curr_indices[j] = curr_indices[j - 1] + 1

        return [
            combination
            for combination in generate_combinations(tuple(range(1, n + 1)), k)
        ]
