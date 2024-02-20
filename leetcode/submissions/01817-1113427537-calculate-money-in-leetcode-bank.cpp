// Submission title: Calculate Money in Leetcode Bank
// Submission url  : https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/
// Submission url  : https://leetcode.com/submissions/detail/1113427537/"

class Solution {
public:
    int totalMoney(int n) {
        int ans {0};
        int monday {1};

        while (n > 0) {
            for (int day {0}; day < min(n, 7); ++day) {
                ans += monday + day;
            }
            n -= 7;
            ++monday;
        }

        return ans;
    }
};
