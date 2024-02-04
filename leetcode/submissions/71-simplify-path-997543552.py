# Submission for Simplify Path
# Submission url: https://leetcode.com/submissions/detail/997543552/


class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = []
        for directory in path.split("/"):
            if not directory or directory == ".":
                continue

            if directory != "..":
                canonical.append(directory)
                continue

            if not len(canonical):
                return "/"

            canonical.pop()

        return "/" + "/".join(canonical)
