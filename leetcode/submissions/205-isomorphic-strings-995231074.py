# Submission for Isomorphic Strings
# Submission url: https://leetcode.com/submissions/detail/995231074/


class Solution:
    # hashmap containing remaps of characters, index
    # iterate over string s:
    # - if symbol s is equal to the symbol t, move the index, continue
    # - if not:
    #   - if there is a remap for that symbol and that is equal, move the index, continue
    #   - if there is a remap and it is not equal, return False
    #   - if there is no remap, create one, move the index, continue
    # return True
    def isIsomorphic(self, s: str, t: str) -> bool:
        remaps = {}
        for i, symbol in enumerate(s):
            symbol_t = t[i]

            if symbol == symbol_t:
                continue

            if symbol not in remaps:
                remaps[symbol] = symbol_t
                continue

            if remaps[symbol] != symbol_t:
                return False

        return True
