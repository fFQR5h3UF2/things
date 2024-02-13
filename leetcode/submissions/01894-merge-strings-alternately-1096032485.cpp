// Submission title: Merge Strings Alternately
// Submission url  : https://leetcode.com/problems/merge-strings-alternately/description/
// Submission url  : https://leetcode.com/submissions/detail/1096032485/
// Submission json : {"id":1096032485,"status_display":"Accepted","lang":"cpp","question_id":1894,"title_slug":"merge-strings-alternately","code":"class Solution {\npublic:\n    string mergeAlternately(string word1, string word2) {\n        int m = word1.size();\n        int n = word2.size();\n        string result = \"\";\n\n        for (int i = 0; i < max(m, n); i++) {\n            if (i < m) {\n                result.push_back(word1[i]);\n            }\n            if (i < n) {\n                result.push_back(word2[i]);\n            }\n        }\n\n        return result;\n    }\n};","title":"Merge Strings Alternately","url":"/submissions/detail/1096032485/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699635003,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"6.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        string result = "";

        for (int i = 0; i < max(m, n); i++) {
            if (i < m) {
                result.push_back(word1[i]);
            }
            if (i < n) {
                result.push_back(word2[i]);
            }
        }

        return result;
    }
};
