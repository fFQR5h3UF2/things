// Submission title: Minimum One Bit Operations to Make Integers Zero
// Submission url  : https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/"
// Submission url  : https://leetcode.com/submissions/detail/1109412407/"

class Solution {
public:
    int minimumOneBitOperations(int n) {
        if (n == 0) {
            return 0;
        }

        int k = 0;
        int curr = 1;
        while (curr * 2 <= n) {
            curr *= 2;
            k++;
        }

        return (1 << (k + 1)) - 1 - minimumOneBitOperations(n ^ curr);
    }
};
