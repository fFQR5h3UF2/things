// Submission title: for Greatest Common Divisor of Strings
// Submission url  : https://leetcode.com/submissions/detail/1105473269/
// Submission json : {"id": 1105473269, "status_display": "Accepted", "lang": "cpp", "question_id": 1146, "title_slug": "greatest-common-divisor-of-strings", "code": "class Solution {\npublic:\n    bool valid(string str1, string str2, size_t k) {\n        size_t len1 {str1.size()}, len2 {str2.size()};\n        if (len1 % k != 0 || len2 % k != 0) {\n            return false;\n        }\n        string base = str1.substr(0, k);\n        size_t n1 {len1 / k}, n2 {len2 / k};\n        if (n1 == n2) {\n            return str1 == str2 && joinWords(base, n1) == str1;\n        }\n        return str1 == joinWords(base, n1) && str2 == joinWords(base, n2);\n    }\n\n    string joinWords(string str, size_t k) {\n        string ans = \"\";\n        for (size_t i = 0; i < k; ++i) {\n            ans += str;\n        }\n        return ans;\n    }\n    \n    \n    string gcdOfStrings(string str1, string str2) {\n        for (size_t i = min(str1.size(), str2.size()); i > 0; --i) {\n            if (valid(str1, str2, i)) {\n                return str1.substr(0, i);\n            }\n        }\n        return \"\";\n    }\n};", "title": "Greatest Common Divisor of Strings", "url": "/submissions/detail/1105473269/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1700832771, "status": 10, "runtime": "4 ms", "is_pending": "Not Pending", "memory": "34 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    bool valid(string str1, string str2, size_t k) {
        size_t len1 {str1.size()}, len2 {str2.size()};
        if (len1 % k != 0 || len2 % k != 0) {
            return false;
        }
        string base = str1.substr(0, k);
        size_t n1 {len1 / k}, n2 {len2 / k};
        if (n1 == n2) {
            return str1 == str2 && joinWords(base, n1) == str1;
        }
        return str1 == joinWords(base, n1) && str2 == joinWords(base, n2);
    }

    string joinWords(string str, size_t k) {
        string ans = "";
        for (size_t i = 0; i < k; ++i) {
            ans += str;
        }
        return ans;
    }


    string gcdOfStrings(string str1, string str2) {
        for (size_t i = min(str1.size(), str2.size()); i > 0; --i) {
            if (valid(str1, str2, i)) {
                return str1.substr(0, i);
            }
        }
        return "";
    }
};
