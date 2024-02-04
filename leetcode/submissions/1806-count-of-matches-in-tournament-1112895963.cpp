// Submission for Count of Matches in Tournament
// Submission url: https://leetcode.com/submissions/detail/1112895963/



class Solution {
public:
    int numberOfMatches(int n) {
        int ans {};
        while (n > 0) {
            int matches {};
            if (n % 2 == 0) {
                matches = n / 2;
            } else {
                matches = (n - 1) / 2 + 1;
            }
            ans += matches;
            n -= matches;
        }
        return ans;
    }
};
