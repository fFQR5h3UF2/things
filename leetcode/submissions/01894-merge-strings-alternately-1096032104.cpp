// Submission title: Merge Strings Alternately
// Submission url  : https://leetcode.com/problems/merge-strings-alternately/description/
// Submission url  : https://leetcode.com/submissions/detail/1096032104/
// Submission json : {"id":1096032104,"status_display":"Accepted","lang":"cpp","question_id":1894,"title_slug":"merge-strings-alternately","code":"class Solution {\npublic:\n    string mergeAlternately(string word1, string word2) {\n        int l1 = word1.size(), l2 = word2.size();\n        string result = \"\";\n        int i = 0, j = 0;\n        while (i < l1 || j < l2) {\n            if (i < l1) {\n                result.push_back(word1[i++]);\n            }\n            if (j < l2) {\n                result.push_back(word2[j++]);\n            }\n        }\n        return result;\n    }\n};","title":"Merge Strings Alternately","url":"/submissions/detail/1096032104/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699634967,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"6.6 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l1 = word1.size(), l2 = word2.size();
        string result = "";
        int i = 0, j = 0;
        while (i < l1 || j < l2) {
            if (i < l1) {
                result.push_back(word1[i++]);
            }
            if (j < l2) {
                result.push_back(word2[j++]);
            }
        }
        return result;
    }
};
