// Submission title: Find the Highest Altitude
// Submission url  : https://leetcode.com/problems/find-the-highest-altitude/description/
// Submission url  : https://leetcode.com/submissions/detail/1100028827/"

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int att {0}, maxAtt {0};
        for (int num : gain) {
            att += num;
            maxAtt = max(maxAtt, att);
        }
        return maxAtt;
    }
};
