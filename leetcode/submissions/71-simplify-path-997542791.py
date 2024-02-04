# Submission for Simplify Path
# Submission url: https://leetcode.com/submissions/detail/997542791/


class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = []
        for directory in path.split("/"):
            if not directory or directory == ".":
                continue

            if directory != "..":
                canonical.append(directory)
                continue

        return "/" + "/".join(canonical)
