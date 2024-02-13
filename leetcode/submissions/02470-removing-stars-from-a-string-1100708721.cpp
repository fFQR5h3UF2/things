// Submission title: Removing Stars From a String
// Submission url  : https://leetcode.com/problems/removing-stars-from-a-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1100708721/
// Submission json : {"id":1100708721,"status_display":"Accepted","lang":"cpp","question_id":2470,"title_slug":"removing-stars-from-a-string","code":"class Solution {\npublic:\n    string removeStars(string s) {\n        std::string ans;\n        unsigned long length {s.size()};\n        int remove {0};\n        for (int i = length - 1; i >= 0; --i) {\n            char c = s[i];\n            if (c == '*') {\n                ++remove;\n                continue;\n            }\n            if (remove == 0) {\n                ans += c;\n            } else {\n                --remove;\n            }\n        }\n        std::reverse(ans.begin(), ans.end());\n        return ans;\n    }\n};","title":"Removing Stars From a String","url":"/submissions/detail/1100708721/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700215953,"status":10,"runtime":"74 ms","is_pending":"Not Pending","memory":"25.2 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string removeStars(string s) {
        std::string ans;
        unsigned long length {s.size()};
        int remove {0};
        for (int i = length - 1; i >= 0; --i) {
            char c = s[i];
            if (c == '*') {
                ++remove;
                continue;
            }
            if (remove == 0) {
                ans += c;
            } else {
                --remove;
            }
        }
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
