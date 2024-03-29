// Submission title: Count of Matches in Tournament
// Submission url  : https://leetcode.com/problems/count-of-matches-in-tournament/description/
// Submission url  : https://leetcode.com/submissions/detail/1112898278/"

class Solution {
public:
    int numberOfMatches(int n) {
        int ans = 0;
        while (n > 1) {
            if (n % 2 == 0) {
                int matches {n / 2};
                ans += matches;
                n = matches;
            } else {
                int matches {(n - 1) / 2};
                ans += matches;
                n = matches + 1;
            }
        }

        return ans;
    }
};
