# Submission title: Course Schedule
# Submission url  : https://leetcode.com/problems/course-schedule/description/
# Submission url  : https://leetcode.com/submissions/detail/1037757786/
# Submission json : {"id":1037757786,"status_display":"Accepted","lang":"python3","question_id":207,"title_slug":"course-schedule","code":"class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        \n        nodes = [[] for _ in range(numCourses)]\n        for target, required in prerequisites:\n            nodes[target].append(required)\n\n        visited = set()\n\n        @cache\n        def dfs(course: int) -> bool:\n            if course in visited:\n                return False\n    \n            edges = nodes[course]\n            if not edges:\n                return True\n            \n            visited.add(course)\n            return all(dfs(edge) for edge in edges)\n\n        for course in range(numCourses):\n            if not dfs(course):\n                return False\n            visited.clear()\n        \n        return True","title":"Course Schedule","url":"/submissions/detail/1037757786/","lang_name":"Python3","time":"5 months","timestamp":1693582667,"status":10,"runtime":"105 ms","is_pending":"Not Pending","memory":"22.1 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        nodes = [[] for _ in range(numCourses)]
        for target, required in prerequisites:
            nodes[target].append(required)

        visited = set()

        @cache
        def dfs(course: int) -> bool:
            if course in visited:
                return False

            edges = nodes[course]
            if not edges:
                return True

            visited.add(course)
            return all(dfs(edge) for edge in edges)

        for course in range(numCourses):
            if not dfs(course):
                return False
            visited.clear()

        return True
