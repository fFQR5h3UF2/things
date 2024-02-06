// Submission title: for Two Sum
// Submission url  : https://leetcode.com/submissions/detail/1096529439/
// Submission json : {"id": 1096529439, "status_display": "Accepted", "lang": "cpp", "question_id": 1, "title_slug": "two-sum", "code": "class Solution {\npublic:\n    vector<int> twoSum(vector<int>& nums, int target) {\n        std::map<int, int> numToIndex;\n        int length = nums.size();\n        std::vector<int> ans;\n        for (int i = 0; i < length; ++i) {\n            int num = nums[i];\n            int diff = target - num;\n            if (numToIndex.contains(diff)) {\n                ans = {numToIndex[diff], i};\n                break;\n            }\n            numToIndex[num] = i;\n        }\n        return ans;\n    }\n};", "title": "Two Sum", "url": "/submissions/detail/1096529439/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699706616, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "11.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> numToIndex;
        int length = nums.size();
        std::vector<int> ans;
        for (int i = 0; i < length; ++i) {
            int num = nums[i];
            int diff = target - num;
            if (numToIndex.contains(diff)) {
                ans = {numToIndex[diff], i};
                break;
            }
            numToIndex[num] = i;
        }
        return ans;
    }
};
