// Submission title: for Sum of Absolute Differences in a Sorted Array
// Submission url  : https://leetcode.com/submissions/detail/1106286305/
// Submission json : {"id": 1106286305, "status_display": "Accepted", "lang": "cpp", "question_id": 1787, "title_slug": "sum-of-absolute-differences-in-a-sorted-array", "code": "class Solution {\npublic:\n    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {\n        int n = nums.size();\n        vector<int> prefix = {nums[0]};\n        for (int i = 1; i < n; i++) {\n            prefix.push_back(prefix[i - 1] + nums[i]);\n        }\n        vector<int> ans;\n        for (int i = 0; i < n; i++) {\n            int leftSum = prefix[i] - nums[i];\n            int rightSum = prefix[n - 1] - prefix[i];\n            \n            int leftCount = i;\n            int rightCount = n - 1 - i;\n            \n            int leftTotal = leftCount * nums[i] - leftSum;\n            int rightTotal = rightSum - rightCount * nums[i];\n            \n            ans.push_back(leftTotal + rightTotal);\n        }\n        return ans;\n    }\n};", "title": "Sum of Absolute Differences in a Sorted Array", "url": "/submissions/detail/1106286305/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1700938821, "status": 10, "runtime": "104 ms", "is_pending": "Not Pending", "memory": "94.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix = {nums[0]};
        for (int i = 1; i < n; i++) {
            prefix.push_back(prefix[i - 1] + nums[i]);
        }
        vector<int> ans;
        for (int i = 0; i < n; i++) {
            int leftSum = prefix[i] - nums[i];
            int rightSum = prefix[n - 1] - prefix[i];

            int leftCount = i;
            int rightCount = n - 1 - i;

            int leftTotal = leftCount * nums[i] - leftSum;
            int rightTotal = rightSum - rightCount * nums[i];

            ans.push_back(leftTotal + rightTotal);
        }
        return ans;
    }
};
