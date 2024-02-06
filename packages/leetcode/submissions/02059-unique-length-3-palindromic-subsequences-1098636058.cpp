// Submission title: for Unique Length-3 Palindromic Subsequences
// Submission url  : https://leetcode.com/submissions/detail/1098636058/
// Submission json : {"id": 1098636058, "status_display": "Accepted", "lang": "cpp", "question_id": 2059, "title_slug": "unique-length-3-palindromic-subsequences", "code": "class Solution {\npublic:\n    int countPalindromicSubsequence(string s) {\n        unordered_set<char> letters;\n        for (char c : s) {\n            letters.insert(c);\n        }\n        int ans = 0;\n        for (char letter : letters) {\n            int i = -1;\n            int j = 0;\n            for (int k = 0; k < s.size(); k++) {\n                if (s[k] == letter) {\n                    if (i == -1) {\n                        i = k;\n                    }\n                    \n                    j = k;\n                }\n            }\n            unordered_set<char> between;\n            for (int k = i + 1; k < j; k++) {\n                between.insert(s[k]);\n            }\n            \n            ans += between.size();\n        }\n        return ans;\n    }\n};\n\n", "title": "Unique Length-3 Palindromic Subsequences", "url": "/submissions/detail/1098636058/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699965568, "status": 10, "runtime": "278 ms", "is_pending": "Not Pending", "memory": "13.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_set<char> letters;
        for (char c : s) {
            letters.insert(c);
        }
        int ans = 0;
        for (char letter : letters) {
            int i = -1;
            int j = 0;
            for (int k = 0; k < s.size(); k++) {
                if (s[k] == letter) {
                    if (i == -1) {
                        i = k;
                    }

                    j = k;
                }
            }
            unordered_set<char> between;
            for (int k = i + 1; k < j; k++) {
                between.insert(s[k]);
            }

            ans += between.size();
        }
        return ans;
    }
};
