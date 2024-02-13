// Submission title: Reverse Words in a String
// Submission url  : https://leetcode.com/problems/reverse-words-in-a-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1096525336/
// Submission json : {"id":1096525336,"status_display":"Accepted","lang":"cpp","question_id":151,"title_slug":"reverse-words-in-a-string","code":"class Solution {\npublic:\n    string reverseWords(string s) {\n        string ans = \"\";\n        string temp = \"\";\n        int length = s.length();\n        int j = 0;\n        for (j = 0; s[j] == ' ' && j < length; ++j) { }\n        for (int i = length - 1; i >= j; --i) {\n            if(s[i] == ' '){\n                if(temp != \"\"){                  \n                    ans = ans + temp + ' ';\n                    temp = \"\";\n                }\n                continue;\n            }\n            else{\n                temp = s[i] + temp;\n            }\n        }\n        return ans + temp;\n    }\n};","title":"Reverse Words in a String","url":"/submissions/detail/1096525336/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699705954,"status":10,"runtime":"8 ms","is_pending":"Not Pending","memory":"46.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string reverseWords(string s) {
        string ans = "";
        string temp = "";
        int length = s.length();
        int j = 0;
        for (j = 0; s[j] == ' ' && j < length; ++j) { }
        for (int i = length - 1; i >= j; --i) {
            if(s[i] == ' '){
                if(temp != ""){
                    ans = ans + temp + ' ';
                    temp = "";
                }
                continue;
            }
            else{
                temp = s[i] + temp;
            }
        }
        return ans + temp;
    }
};
