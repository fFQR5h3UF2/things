# Submission title: Group the People Given the Group Size They Belong To
# Submission url  : https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
# Submission url  : https://leetcode.com/submissions/detail/1046482817/
# Submission json : {"id":1046482817,"status_display":"Accepted","lang":"python3","question_id":1407,"title_slug":"group-the-people-given-the-group-size-they-belong-to","code":"class Solution:\n    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:\n        answer = []\n        cur_groups = defaultdict(list)\n        \n        for i in range(len(groupSizes)):\n            size = groupSizes[i]\n            group = cur_groups[size]\n            group.append(i)\n            if len(group) == size:\n                answer.append(group)\n                del cur_groups[size]\n        \n        return answer","title":"Group the People Given the Group Size They Belong To","url":"/submissions/detail/1046482817/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694434015,"status":10,"runtime":"69 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        cur_groups = defaultdict(list)

        for i in range(len(groupSizes)):
            size = groupSizes[i]
            group = cur_groups[size]
            group.append(i)
            if len(group) == size:
                answer.append(group)
                del cur_groups[size]

        return answer
