// Submission title: Sum of Absolute Differences in a Sorted Array
// Submission url  : https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/
// Submission url  : https://leetcode.com/submissions/detail/1106286504/
// Submission json : {"id":1106286504,"status_display":"Accepted","lang":"cpp","question_id":1787,"title_slug":"sum-of-absolute-differences-in-a-sorted-array","code":"class Solution {\npublic:\n    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {\n        int n = nums.size();\n        int totalSum = accumulate(nums.begin(), nums.end(), 0);\n        \n        int leftSum = 0;\n        vector<int> ans;\n        for (int i = 0; i < n; i++) {\n            int rightSum = totalSum - leftSum - nums[i];\n            \n            int leftCount = i;\n            int rightCount = n - 1 - i;\n            \n            int leftTotal = leftCount * nums[i] - leftSum;\n            int rightTotal = rightSum - rightCount * nums[i];\n            \n            ans.push_back(leftTotal + rightTotal);\n            leftSum += nums[i];\n        }\n        \n        return ans;\n    }\n};","title":"Sum of Absolute Differences in a Sorted Array","url":"/submissions/detail/1106286504/","lang_name":"C++","time":"2 months, 1 week","timestamp":1700938844,"status":10,"runtime":"96 ms","is_pending":"Not Pending","memory":"87.8 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int n = nums.size();
        int totalSum = accumulate(nums.begin(), nums.end(), 0);

        int leftSum = 0;
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            int rightSum = totalSum - leftSum - nums[i];

            int leftCount = i;
            int rightCount = n - 1 - i;

            int leftTotal = leftCount * nums[i] - leftSum;
            int rightTotal = rightSum - rightCount * nums[i];

            ans.push_back(leftTotal + rightTotal);
            leftSum += nums[i];
        }

        return ans;
    }
};
