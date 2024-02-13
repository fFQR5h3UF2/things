// Submission title: Merge Strings Alternately
// Submission url  : https://leetcode.com/problems/merge-strings-alternately/description/
// Submission url  : https://leetcode.com/submissions/detail/1096031254/
// Submission json : {"id":1096031254,"status_display":"Accepted","lang":"cpp","question_id":1894,"title_slug":"merge-strings-alternately","code":"class Solution {\npublic:\n    string mergeAlternately(string word1, string word2) {\n        std::stringstream ans;\n        int l1 = word1.size(), l2 = word2.size();\n        int lMax = max(l1, l2);\n        for (int i = 0; i < lMax; ++i) {\n            if (i < l1) {\n                ans << word1[i];\n            } else {\n                ans << word2.substr(i);\n                break;\n            }\n            if (i < l2) {\n                ans << word2[i];\n            } else {\n                ans << word1.substr(i + 1);\n                break;\n            }\n        }\n        return ans.str();\n    }\n};","title":"Merge Strings Alternately","url":"/submissions/detail/1096031254/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699634878,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::stringstream ans;
        int l1 = word1.size(), l2 = word2.size();
        int lMax = max(l1, l2);
        for (int i = 0; i < lMax; ++i) {
            if (i < l1) {
                ans << word1[i];
            } else {
                ans << word2.substr(i);
                break;
            }
            if (i < l2) {
                ans << word2[i];
            } else {
                ans << word1.substr(i + 1);
                break;
            }
        }
        return ans.str();
    }
};
