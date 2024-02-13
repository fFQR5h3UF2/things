// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/
// Submission url  : https://leetcode.com/submissions/detail/1096516392/
// Submission json : {"id":1096516392,"status_display":"Accepted","lang":"cpp","question_id":283,"title_slug":"move-zeroes","code":"class Solution {\npublic:\n    void moveZeroes(vector<int>& nums) {\n        int length = nums.size();\n        int lastNonZeroFoundAt = 0;\n        for (int i = 0; i < length; ++i) {\n            if (nums[i] != 0) {\n                swap(nums[lastNonZeroFoundAt], nums[i]);\n                lastNonZeroFoundAt += 1;\n            }\n        }\n    }\n};","title":"Move Zeroes","url":"/submissions/detail/1096516392/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699704535,"status":10,"runtime":"16 ms","is_pending":"Not Pending","memory":"19.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int length = nums.size();
        int lastNonZeroFoundAt = 0;
        for (int i = 0; i < length; ++i) {
            if (nums[i] != 0) {
                swap(nums[lastNonZeroFoundAt], nums[i]);
                lastNonZeroFoundAt += 1;
            }
        }
    }
};
