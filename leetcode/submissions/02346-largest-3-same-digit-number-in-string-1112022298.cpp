// Submission title: Largest 3-Same-Digit Number in String
// Submission url  : https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1112022298/
// Submission json : {"id":1112022298,"status_display":"Accepted","lang":"cpp","question_id":2346,"title_slug":"largest-3-same-digit-number-in-string","code":"class Solution {\npublic:\n    string largestGoodInteger(string num) {\n        int cur {-1};\n        int max {-1};\n        int count {0};\n        for (const char& ch : num) {\n            int i {ch - '0'};\n            if (i == cur) {\n                ++count;\n            } else {\n                cur = i;\n                count = 1; \n            }\n            if (count == 3) {\n                max = std::max(i, max);\n            }\n        }\n        if (max == -1) {\n            return \"\";\n        }\n        std::string ans {std::to_string(max)};\n        return ans + ans + ans;\n    }\n};","title":"Largest 3-Same-Digit Number in String","url":"/submissions/detail/1112022298/","lang_name":"C++","time":"2 months","timestamp":1701677339,"status":10,"runtime":"4 ms","is_pending":"Not Pending","memory":"6.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string largestGoodInteger(string num) {
        int cur {-1};
        int max {-1};
        int count {0};
        for (const char& ch : num) {
            int i {ch - '0'};
            if (i == cur) {
                ++count;
            } else {
                cur = i;
                count = 1;
            }
            if (count == 3) {
                max = std::max(i, max);
            }
        }
        if (max == -1) {
            return "";
        }
        std::string ans {std::to_string(max)};
        return ans + ans + ans;
    }
};
