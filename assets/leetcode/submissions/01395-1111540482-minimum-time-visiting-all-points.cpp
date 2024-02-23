// Submission title: Minimum Time Visiting All Points
// Submission url  : https://leetcode.com/problems/minimum-time-visiting-all-points/description/
// Submission url  : https://leetcode.com/submissions/detail/1111540482/"

class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int ans = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            int currX = points[i][0];
            int currY = points[i][1];
            int targetX = points[i + 1][0];
            int targetY = points[i + 1][1];
            ans += max(abs(targetX - currX), abs(targetY - currY));
        }

        return ans;
    }
};
