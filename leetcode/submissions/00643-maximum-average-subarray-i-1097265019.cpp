// Submission title: Maximum Average Subarray I
// Submission url  : https://leetcode.com/problems/maximum-average-subarray-i/description/
// Submission url  : https://leetcode.com/submissions/detail/1097265019/
// Submission json : {"id":1097265019,"status_display":"Accepted","lang":"cpp","question_id":643,"title_slug":"maximum-average-subarray-i","code":"class Solution {\npublic:\n    double findMaxAverage(vector<int>& nums, int k) {\n        int length = nums.size();\n        double sum = std::accumulate(nums.begin(), nums.begin() + k , 0);\n        double maxSum = sum;\n        for (int i = k; i < length; ++i) {\n            sum += nums[i] - nums[i-k];\n            maxSum = max(sum, maxSum);\n        }\n        return maxSum / k;\n    }\n};","title":"Maximum Average Subarray I","url":"/submissions/detail/1097265019/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699797622,"status":10,"runtime":"144 ms","is_pending":"Not Pending","memory":"109.9 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

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
