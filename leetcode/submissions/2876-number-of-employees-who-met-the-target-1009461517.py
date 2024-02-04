# Submission for 'Number of Employees Who Met the Target'
# Submission url: https://leetcode.com/submissions/detail/1009461517/

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for hour in hours:
            if hour < target:
                continue
            count += 1

        return count
