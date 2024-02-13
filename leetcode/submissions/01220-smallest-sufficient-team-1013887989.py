# Submission title: Smallest Sufficient Team
# Submission url  : https://leetcode.com/problems/smallest-sufficient-team/description/
# Submission url  : https://leetcode.com/submissions/detail/1013887989/
# Submission json : {"id":1013887989,"status_display":"Accepted","lang":"python3","question_id":1220,"title_slug":"smallest-sufficient-team","code":"class Solution:\n    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:\n        req_skills_count = len(req_skills)\n        skill_to_people = defaultdict(set)\n        for i, person in enumerate(people):\n            for skill in person:\n                skill_to_people[skill].add(i)\n\n        current = set()\n        \n        def backtrack(skill: int) -> Tuple[int]:\n            if skill == req_skills_count:\n                return tuple(current)\n            \n            suff_team = None\n            people_with_skill = skill_to_people[req_skills[skill]] \n            \n            if current & people_with_skill:\n                return backtrack(skill + 1)\n        \n            for person in people_with_skill:\n                current.add(person)\n                new_team = backtrack(skill + 1)\n                current.remove(person)\n\n                if suff_team is None or len(new_team) < len(suff_team):\n                    suff_team = new_team\n\n            return suff_team\n\n        return backtrack(0)\n        \n","title":"Smallest Sufficient Team","url":"/submissions/detail/1013887989/","lang_name":"Python3","time":"6 months","timestamp":1691331521,"status":10,"runtime":"5965 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        req_skills_count = len(req_skills)
        skill_to_people = defaultdict(set)
        for i, person in enumerate(people):
            for skill in person:
                skill_to_people[skill].add(i)

        current = set()

        def backtrack(skill: int) -> Tuple[int]:
            if skill == req_skills_count:
                return tuple(current)

            suff_team = None
            people_with_skill = skill_to_people[req_skills[skill]]

            if current & people_with_skill:
                return backtrack(skill + 1)

            for person in people_with_skill:
                current.add(person)
                new_team = backtrack(skill + 1)
                current.remove(person)

                if suff_team is None or len(new_team) < len(suff_team):
                    suff_team = new_team

            return suff_team

        return backtrack(0)
