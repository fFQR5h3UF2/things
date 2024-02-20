// Submission title: Maximum Average Subarray I
// Submission url  : https://leetcode.com/problems/maximum-average-subarray-i/description/
// Submission url  : https://leetcode.com/submissions/detail/1097265019/"

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int length = nums.size();
        double sum = std::accumulate(nums.begin(), nums.begin() + k , 0);
        double maxSum = sum;
        for (int i = k; i < length; ++i) {
            sum += nums[i] - nums[i-k];
            maxSum = max(sum, maxSum);
        }
        return maxSum / k;
    }
};
