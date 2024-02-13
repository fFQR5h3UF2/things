// Submission title: Greatest Common Divisor of Strings
// Submission url  : https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
// Submission url  : https://leetcode.com/submissions/detail/1105475590/
// Submission json : {"id":1105475590,"status_display":"Accepted","lang":"cpp","question_id":1146,"title_slug":"greatest-common-divisor-of-strings","code":"class Solution {\npublic:\n    string gcdOfStrings(string str1, string str2) {\n        if (str1 + str2 == str2 + str1) {\n            return str1.substr(0, std::gcd(str1.size(), str2.size()));\n        }\n        return \"\";\n    }\n};","title":"Greatest Common Divisor of Strings","url":"/submissions/detail/1105475590/","lang_name":"C++","time":"2 months, 1 week","timestamp":1700833060,"status":10,"runtime":"5 ms","is_pending":"Not Pending","memory":"7.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 == str2 + str1) {
            return str1.substr(0, std::gcd(str1.size(), str2.size()));
        }
        return "";
    }
};
