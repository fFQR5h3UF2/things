// Submission title: for Sort Vowels in a String
// Submission url  : https://leetcode.com/submissions/detail/1097738650/
// Submission json : {"id": 1097738650, "status_display": "Accepted", "lang": "cpp", "question_id": 2887, "title_slug": "sort-vowels-in-a-string", "code": "class Solution {\npublic:\n    string sortVowels(string s) {\n        std::map<char, int> vowels{\n            {'A', 0}, {'E', 0}, {'I', 0}, {'O', 0}, {'U', 0},\n            {'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}\n        };\n        const char order[10]{ 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u' };\n        unsigned long length{ s.size() };\n        for (char ch : s) {\n            if (vowels.contains(ch)) {\n                ++vowels[ch];\n            }\n        }\n        for (int i = 0; i < length; ++i) {\n            const char ch = s[i];\n            if (!vowels.contains(ch)) {\n                continue;\n            }\n            for (char orderChar : order) {\n                if (vowels[orderChar] > 0) {\n                    s[i] = orderChar;\n                    --vowels[orderChar];\n                    break;\n                }\n            }\n        }\n        return s;\n    }\n};", "title": "Sort Vowels in a String", "url": "/submissions/detail/1097738650/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699861126, "status": 10, "runtime": "94 ms", "is_pending": "Not Pending", "memory": "12.7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    string sortVowels(string s) {
        std::map<char, int> vowels{
            {'A', 0}, {'E', 0}, {'I', 0}, {'O', 0}, {'U', 0},
            {'a', 0}, {'e', 0}, {'i', 0}, {'o', 0}, {'u', 0}
        };
        const char order[10]{ 'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u' };
        unsigned long length{ s.size() };
        for (char ch : s) {
            if (vowels.contains(ch)) {
                ++vowels[ch];
            }
        }
        for (int i = 0; i < length; ++i) {
            const char ch = s[i];
            if (!vowels.contains(ch)) {
                continue;
            }
            for (char orderChar : order) {
                if (vowels[orderChar] > 0) {
                    s[i] = orderChar;
                    --vowels[orderChar];
                    break;
                }
            }
        }
        return s;
    }
};