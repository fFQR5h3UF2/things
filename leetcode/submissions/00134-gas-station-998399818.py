# Submission title: Gas Station
# Submission url  : https://leetcode.com/problems/gas-station/description/
# Submission url  : https://leetcode.com/submissions/detail/998399818/
# Submission json : {"id":998399818,"status_display":"Accepted","lang":"python3","question_id":134,"title_slug":"gas-station","code":"class Solution:\n    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:\n        if sum(gas) < sum(cost): \n            return -1\n        \n        tank, idx = 0, 0\n        for i in range(len(gas)):\n            tank += gas[i] - cost[i] \n            if tank < 0: \n                tank, idx = 0, i+1\n        return idx ","title":"Gas Station","url":"/submissions/detail/998399818/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689765998,"status":10,"runtime":"1223 ms","is_pending":"Not Pending","memory":"22.3 MB","compare_result":"1111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank, idx = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, idx = 0, i + 1
        return idx
