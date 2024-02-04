// Submission for Maximum Average Subarray I
// Submission url: https://leetcode.com/submissions/detail/1097262144/



class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int length = nums.size();
        double sum = std::accumulate(nums.begin(), nums.begin() + k, 0);
        for (int i = k; i < length; ++i) {
            double newSum = sum - nums[i-k] + nums[i];
            if (newSum > sum) {
                sum = newSum;
            }
        }
        return sum / k;
    }
};
