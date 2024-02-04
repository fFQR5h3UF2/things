// Submission title: for Find Words That Can Be Formed by Characters
// Submission url  : https://leetcode.com/submissions/detail/1111055227/
// Submission json : {"id": 1111055227, "status_display": "Accepted", "lang": "cpp", "question_id": 1112, "title_slug": "find-words-that-can-be-formed-by-characters", "code": "class Solution {\npublic:\n    int countCharacters(vector<string>& words, string chars) {\n        std::vector<int> count {};\n        int ans {};\n        count.resize(26);\n        for (const char& ch : chars) {\n            ++count[ch - 'a'];\n        }\n        for (const string& word : words) {\n            std::vector<int> wordCount {};\n            wordCount.resize(26);\n            bool failure {false};\n            for (const char& ch : word) {\n                int i {ch - 'a'};\n                int cur {++wordCount[i]};\n                if (cur > count[i]) {\n                    failure = true;\n                    break;\n                }\n            }\n            if (!failure) {\n                ans += word.length();\n            }\n        }\n        return ans;\n    }\n};", "title": "Find Words That Can Be Formed by Characters", "url": "/submissions/detail/1111055227/", "lang_name": "C++", "time": "2\u00a0months", "timestamp": 1701549608, "status": 10, "runtime": "40 ms", "is_pending": "Not Pending", "memory": "20.7 MB", "compare_result": "111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        std::vector<int> count {};
        int ans {};
        count.resize(26);
        for (const char& ch : chars) {
            ++count[ch - 'a'];
        }
        for (const string& word : words) {
            std::vector<int> wordCount {};
            wordCount.resize(26);
            bool failure {false};
            for (const char& ch : word) {
                int i {ch - 'a'};
                int cur {++wordCount[i]};
                if (cur > count[i]) {
                    failure = true;
                    break;
                }
            }
            if (!failure) {
                ans += word.length();
            }
        }
        return ans;
    }
};
