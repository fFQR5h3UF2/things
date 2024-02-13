// Submission title: Reduction Operations to Make the Array Elements Equal
// Submission url  : https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/
// Submission url  : https://leetcode.com/submissions/detail/1101990098/
// Submission json : {"id":1101990098,"status_display":"Accepted","lang":"cpp","question_id":2016,"title_slug":"reduction-operations-to-make-the-array-elements-equal","code":"class Solution {\npublic:\n    int reductionOperations(vector<int>& nums) {\n        sort(nums.begin(), nums.end());\n        int ans = 0;\n        int up = 0;\n        auto length {nums.size()};\n        for (int i = 1; i < length; ++i) {\n            if (nums[i] != nums[i - 1]) {\n                ++up;\n            }\n            ans += up;\n        }\n        return ans;\n    }\n};","title":"Reduction Operations to Make the Array Elements Equal","url":"/submissions/detail/1101990098/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700382665,"status":10,"runtime":"147 ms","is_pending":"Not Pending","memory":"83.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int reductionOperations(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int ans = 0;
        int up = 0;
        auto length {nums.size()};
        for (int i = 1; i < length; ++i) {
            if (nums[i] != nums[i - 1]) {
                ++up;
            }
            ans += up;
        }
        return ans;
    }
};
