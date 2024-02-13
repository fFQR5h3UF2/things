// Submission title: Increasing Triplet Subsequence
// Submission url  : https://leetcode.com/problems/increasing-triplet-subsequence/description/
// Submission url  : https://leetcode.com/submissions/detail/1099380129/
// Submission json : {"id":1099380129,"status_display":"Accepted","lang":"cpp","question_id":334,"title_slug":"increasing-triplet-subsequence","code":"class Solution {\npublic:\n    bool increasingTriplet(vector<int>& nums) {\n        auto length{nums.size()};\n        int num1{INT_MAX}, num2{INT_MAX}; \n        for (int num : nums) {\n            if (num <= num1) {\n                num1 = num;\n            } else if (num <= num2) {\n                num2 = num;\n            } else {\n                return true;\n            }\n        }\n        return false;\n    }\n};","title":"Increasing Triplet Subsequence","url":"/submissions/detail/1099380129/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1700053947,"status":10,"runtime":"82 ms","is_pending":"Not Pending","memory":"112 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        auto length{nums.size()};
        int num1{INT_MAX}, num2{INT_MAX};
        for (int num : nums) {
            if (num <= num1) {
                num1 = num;
            } else if (num <= num2) {
                num2 = num;
            } else {
                return true;
            }
        }
        return false;
    }
};
