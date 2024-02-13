# Submission title: Simplify Path
# Submission url  : https://leetcode.com/problems/simplify-path/description/
# Submission url  : https://leetcode.com/submissions/detail/997543979/
# Submission json : {"id":997543979,"status_display":"Accepted","lang":"python3","question_id":71,"title_slug":"simplify-path","code":"class Solution:\n    def simplifyPath(self, path: str) -> str:\n        canonical = []\n        for directory in path.split(\"/\"):\n            if not directory or directory == \".\":\n                continue\n            \n            if directory != \"..\":\n                canonical.append(directory)\n                continue\n            \n            if len(canonical):\n                canonical.pop()\n\n        return \"/\" + \"/\".join(canonical)","title":"Simplify Path","url":"/submissions/detail/997543979/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689683002,"status":10,"runtime":"50 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = []
        for directory in path.split("/"):
            if not directory or directory == ".":
                continue

            if directory != "..":
                canonical.append(directory)
                continue

            if len(canonical):
                canonical.pop()

        return "/" + "/".join(canonical)
