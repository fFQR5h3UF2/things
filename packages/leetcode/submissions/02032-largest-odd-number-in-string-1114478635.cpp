// Submission title: for Largest Odd Number in String
// Submission url  : https://leetcode.com/submissions/detail/1114478635/
// Submission json : {"id": 1114478635, "status_display": "Accepted", "lang": "cpp", "question_id": 2032, "title_slug": "largest-odd-number-in-string", "code": "class Solution {\npublic:\n    string largestOddNumber(string num) {\n        size_t length {num.size()};\n        for (int i = length - 1; i >= 0; --i) {\n            if ((num[i] - '0') % 2 != 0) {\n                return num.substr(0, i + 1);\n            }\n        }\n        return \"\";\n    }\n};", "title": "Largest Odd Number in String", "url": "/submissions/detail/1114478635/", "lang_name": "C++", "time": "1\u00a0month, 4\u00a0weeks", "timestamp": 1701966048, "status": 10, "runtime": "31 ms", "is_pending": "Not Pending", "memory": "15.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    string largestOddNumber(string num) {
        size_t length {num.size()};
        for (int i = length - 1; i >= 0; --i) {
            if ((num[i] - '0') % 2 != 0) {
                return num.substr(0, i + 1);
            }
        }
        return "";
    }
};
