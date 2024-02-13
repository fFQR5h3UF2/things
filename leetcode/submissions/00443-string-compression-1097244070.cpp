// Submission title: String Compression
// Submission url  : https://leetcode.com/problems/string-compression/description/
// Submission url  : https://leetcode.com/submissions/detail/1097244070/
// Submission json : {"id":1097244070,"status_display":"Accepted","lang":"cpp","question_id":443,"title_slug":"string-compression","code":"class Solution {\npublic:\n    int compress(vector<char>& chars) {\n        int i = 0, res = 0;\n        int length = chars.size();\n        while (i < length) {\n            int groupLength = 1;\n            while (i + groupLength < length && chars[i + groupLength] == chars[i]) {\n                groupLength++;\n            }\n            chars[res++] = chars[i];\n            if (groupLength > 1) {\n                for (char c : to_string(groupLength)) {\n                    chars[res++] = c;\n                }\n            }\n            i += groupLength;\n        }\n        return res;\n    }\n};","title":"String Compression","url":"/submissions/detail/1097244070/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699794483,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"9.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int compress(vector<char>& chars) {
        int i = 0, res = 0;
        int length = chars.size();
        while (i < length) {
            int groupLength = 1;
            while (i + groupLength < length && chars[i + groupLength] == chars[i]) {
                groupLength++;
            }
            chars[res++] = chars[i];
            if (groupLength > 1) {
                for (char c : to_string(groupLength)) {
                    chars[res++] = c;
                }
            }
            i += groupLength;
        }
        return res;
    }
};
