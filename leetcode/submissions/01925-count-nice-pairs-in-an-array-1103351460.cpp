// Submission title: Count Nice Pairs in an Array
// Submission url  : https://leetcode.com/problems/count-nice-pairs-in-an-array/description/
// Submission url  : https://leetcode.com/submissions/detail/1103351460/
// Submission json : {"id":1103351460,"status_display":"Accepted","lang":"cpp","question_id":1925,"title_slug":"count-nice-pairs-in-an-array","code":"class Solution {\npublic:\n    int countNicePairs(vector<int>& nums) {\n        std::unordered_map<int, int> diffs{};\n        int ans{};\n        double mod{1e9 + 7};\n        for (const int& num : nums) {\n            int revNum{};\n            int tempNum{num};\n            while(tempNum) {\n                revNum = (revNum * 10) + (tempNum % 10);\n                tempNum /= 10;\n            }\n            int diff{num-revNum};\n            if (diffs.contains(diff)) {\n                ans = std::fmod(ans + diffs[diff], mod);\n            }\n            ++diffs[diff];\n        }\n        return ans;\n    }\n\n};","title":"Count Nice Pairs in an Array","url":"/submissions/detail/1103351460/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700559844,"status":10,"runtime":"100 ms","is_pending":"Not Pending","memory":"57.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        std::unordered_map<int, int> diffs{};
        int ans{};
        double mod{1e9 + 7};
        for (const int& num : nums) {
            int revNum{};
            int tempNum{num};
            while(tempNum) {
                revNum = (revNum * 10) + (tempNum % 10);
                tempNum /= 10;
            }
            int diff{num-revNum};
            if (diffs.contains(diff)) {
                ans = std::fmod(ans + diffs[diff], mod);
            }
            ++diffs[diff];
        }
        return ans;
    }

};
