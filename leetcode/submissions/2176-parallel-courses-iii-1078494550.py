# Submission for Parallel Courses III
# Submission url: https://leetcode.com/submissions/detail/1078494550/


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        required = {i: [time[i], set()] for i in range(n)}

        for prev, nxt in relations:
            required[nxt - 1][1].add(prev - 1)

        max_time = 0

        while required:
            taken = set(course for course in required if len(required[course][1]) == 0)
            for course in taken:
                required.pop(course)
                max_time = max(max_time, required[course][0])

            for course, (_, reqs) in required.items():
                needed = reqs & taken
                if needed:
                    required[course][0] += max(time[item] for item in needed)
                    reqs.difference_update(needed)

        return max_time
