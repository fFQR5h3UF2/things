// Submission title: Check If Two String Arrays are Equivalent
// Submission url  : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/
// Submission url  : https://leetcode.com/submissions/detail/1110086928/
// Submission json : {"id":1110086928,"status_display":"Accepted","lang":"cpp","question_id":1781,"title_slug":"check-if-two-string-arrays-are-equivalent","code":"class Solution {\npublic:\n    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {\n        string s1 = \"\";\n        string s2 = \"\";\n\n        for(const string& s : word1) {\n            s1 += s;\n        }\n        for(const string& s : word2) {\n            s2 += s;\n        }\n        return s1==s2;\n    }\n};","title":"Check If Two String Arrays are Equivalent","url":"/submissions/detail/1110086928/","lang_name":"C++","time":"2 months","timestamp":1701418889,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"12.1 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1 = "";
        string s2 = "";

        for(const string& s : word1) {
            s1 += s;
        }
        for(const string& s : word2) {
            s2 += s;
        }
        return s1==s2;
    }
};
