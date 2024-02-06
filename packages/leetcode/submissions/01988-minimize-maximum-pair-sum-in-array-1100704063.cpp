// Submission title: for Minimize Maximum Pair Sum in Array
// Submission url  : https://leetcode.com/submissions/detail/1100704063/
// Submission json : {"id": 1100704063, "status_display": "Accepted", "lang": "cpp", "question_id": 1988, "title_slug": "minimize-maximum-pair-sum-in-array", "code": "class Solution {\npublic:\n    int minPairSum(vector<int>& nums) {\n        std::sort(nums.begin(), nums.end());\n        unsigned long length {nums.size()};\n        int maxSum {0};\n        for (int i = 0; i < length / 2; ++i) {\n            maxSum = max(maxSum, nums[i] + nums[length - i - 1]);\n        }\n        return maxSum;\n    }\n};", "title": "Minimize Maximum Pair Sum in Array", "url": "/submissions/detail/1100704063/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700215345, "status": 10, "runtime": "190 ms", "is_pending": "Not Pending", "memory": "96.9 MB", "compare_result": "1111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int minPairSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        unsigned long length {nums.size()};
        int maxSum {0};
        for (int i = 0; i < length / 2; ++i) {
            maxSum = max(maxSum, nums[i] + nums[length - i - 1]);
        }
        return maxSum;
    }
};
