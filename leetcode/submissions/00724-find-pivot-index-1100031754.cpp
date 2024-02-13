// Submission title: Find Pivot Index
// Submission url  : https://leetcode.com/problems/find-pivot-index/description/
// Submission url  : https://leetcode.com/submissions/detail/1100031754/
// Submission json : {"id":1100031754,"status_display":"Accepted","lang":"cpp","question_id":724,"title_slug":"find-pivot-index","code":"class Solution {\npublic:\n    int pivotIndex(vector<int>& nums) {\n        int left {0}, right {std::accumulate(nums.begin() + 1, nums.end(), 0)};\n        unsigned long length {nums.size()};\n        if (right == 0) {\n            return 0;\n        }\n        for (int i = 1; i < length; ++i) {\n            left += nums[i-1];\n            right -= nums[i];\n            if (left == right) {\n                return i;\n            }\n        }\n        return -1;\n    }\n};","title":"Find Pivot Index","url":"/submissions/detail/1100031754/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700133203,"status":10,"runtime":"18 ms","is_pending":"Not Pending","memory":"31.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left {0}, right {std::accumulate(nums.begin() + 1, nums.end(), 0)};
        unsigned long length {nums.size()};
        if (right == 0) {
            return 0;
        }
        for (int i = 1; i < length; ++i) {
            left += nums[i-1];
            right -= nums[i];
            if (left == right) {
                return i;
            }
        }
        return -1;
    }
};
