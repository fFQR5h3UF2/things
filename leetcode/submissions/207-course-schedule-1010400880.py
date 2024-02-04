# Submission for Course Schedule
# Submission url: https://leetcode.com/submissions/detail/1010400880/


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(set)

        for course, prereq in prerequisites:
            courses[course].add(prereq)

        if not courses:
            return True

        current = set()

        def check(course: int) -> bool:
            if course not in courses:
                return True

            prereqs = courses[course]

            if prereqs & current:
                return False

            current.add(course)
            prereqs_valid = all(check(prereq) for prereq in prereqs)
            current.remove(course)
            return prereqs_valid

        return all(check(course) for course in courses)
