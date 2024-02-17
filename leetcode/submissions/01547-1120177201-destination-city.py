# Submission title: Destination City
# Submission url  : https://leetcode.com/problems/destination-city/description/"
# Submission url  : https://leetcode.com/submissions/detail/1120177201/"


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        paths_from = set()
        for path_from, path_to in paths:
            paths_from.add(path_from)

        ans = ""
        for _, path_to in paths:
            if path_to not in paths_from:
                ans = path_to
                break

        return ans
