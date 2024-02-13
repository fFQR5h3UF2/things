# Submission title: The K Weakest Rows in a Matrix
# Submission url  : https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
# Submission url  : https://leetcode.com/submissions/detail/1052396767/
# Submission json : {"id":1052396767,"status_display":"Accepted","lang":"python3","question_id":1463,"title_slug":"the-k-weakest-rows-in-a-matrix","code":"class Solution:\n    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:\n        rows_count, cols_count = len(mat), len(mat[0])\n        heap = []\n\n        for i, row in enumerate(mat):\n            count = 0\n            for j, val in enumerate(row):\n                if val == 0:\n                    count = j\n                    break\n            else:\n                count = cols_count\n        \n            heappush(heap, (count, i))\n        \n        return tuple(item[1] for item in nsmallest(k, heap))\n\n","title":"The K Weakest Rows in a Matrix","url":"/submissions/detail/1052396767/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695019672,"status":10,"runtime":"108 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows_count, cols_count = len(mat), len(mat[0])
        heap = []

        for i, row in enumerate(mat):
            count = 0
            for j, val in enumerate(row):
                if val == 0:
                    count = j
                    break
            else:
                count = cols_count

            heappush(heap, (count, i))

        return tuple(item[1] for item in nsmallest(k, heap))
