// Submission title: for Greatest Common Divisor of Strings
// Submission url  : https://leetcode.com/submissions/detail/1105475123/
// Submission json : {"id": 1105475123, "status_display": "Accepted", "lang": "cpp", "question_id": 1146, "title_slug": "greatest-common-divisor-of-strings", "code": "class Solution {\npublic:\n    string gcdOfStrings(string str1, string str2) {\n        if (str1 + str2 != str2 + str1) {\n            return \"\";\n        }\n        unsigned long gcdLength {std::gcd(str1.size(), str2.size())};\n        return str1.substr(0, gcdLength);\n    }\n};", "title": "Greatest Common Divisor of Strings", "url": "/submissions/detail/1105475123/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1700832998, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "7.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) {
            return "";
        }
        unsigned long gcdLength {std::gcd(str1.size(), str2.size())};
        return str1.substr(0, gcdLength);
    }
};
