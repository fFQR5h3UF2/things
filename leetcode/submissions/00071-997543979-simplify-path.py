# Submission title: Simplify Path
# Submission url  : https://leetcode.com/problems/simplify-path/description/
# Submission url  : https://leetcode.com/submissions/detail/997543979/"


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
