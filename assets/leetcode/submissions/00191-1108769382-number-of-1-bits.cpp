// Submission title: Number of 1 Bits
// Submission url  : https://leetcode.com/problems/number-of-1-bits/description/
// Submission url  : https://leetcode.com/submissions/detail/1108769382/"

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ans {};
        while (n) {
            if (n & 1) {
                ++ans;
            }
            n >>= 1;
        }
        return ans;
    }
};
