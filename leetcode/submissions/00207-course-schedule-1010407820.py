# Submission title: Course Schedule
# Submission url  : https://leetcode.com/problems/course-schedule/description/
# Submission url  : https://leetcode.com/submissions/detail/1010407820/
# Submission json : {"id":1010407820,"status_display":"Accepted","lang":"python3","question_id":207,"title_slug":"course-schedule","code":"class Solution:\n    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:\n        courses = defaultdict(set)\n\n        for course, prereq in prerequisites:\n            courses[course].add(prereq)\n\n        if not courses:\n            return True\n        \n        stack = set()\n\n        @cache\n        def check(course: int) -> bool:\n            if course not in courses:\n                return True\n            \n            if course in stack:\n                return False\n\n            prereqs = courses[course]\n\n            if prereqs & stack:\n                return False\n\n            stack.add(course)\n\n            for prereq in prereqs:\n                if not check(prereq):\n                    return False\n    \n            stack.remove(course)\n            \n            return True\n\n        for course in courses:\n            if not check(course):\n                return False\n\n        return True","title":"Course Schedule","url":"/submissions/detail/1010407820/","lang_name":"Python3","time":"6 months","timestamp":1690992177,"status":10,"runtime":"99 ms","is_pending":"Not Pending","memory":"21 MB","compare_result":"1111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(set)

        for course, prereq in prerequisites:
            courses[course].add(prereq)

        if not courses:
            return True

        stack = set()

        @cache
        def check(course: int) -> bool:
            if course not in courses:
                return True

            if course in stack:
                return False

            prereqs = courses[course]

            if prereqs & stack:
                return False

            stack.add(course)

            for prereq in prereqs:
                if not check(prereq):
                    return False

            stack.remove(course)

            return True

        for course in courses:
            if not check(course):
                return False

        return True
