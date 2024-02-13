// Submission title: Reverse Vowels of a String
// Submission url  : https://leetcode.com/problems/reverse-vowels-of-a-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1098055331/
// Submission json : {"id":1098055331,"status_display":"Accepted","lang":"cpp","question_id":345,"title_slug":"reverse-vowels-of-a-string","code":"class Solution {\npublic:\n    bool isVowel(char ch) {\n        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||\n               ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';\n    }\n\n    string reverseVowels(string s) {\n        unsigned long length{s.size()};\n        unsigned long left{0}, right{length-1};\n        while (left < right) {\n            char chLeft{s[left]};\n            char chRight{s[right]};\n            if (!isVowel(chLeft)) {\n                ++left;\n            } else if (!isVowel(chRight)) {\n                --right;\n            } else {\n                s[left] = chRight;\n                s[right] = chLeft;\n                ++left;\n                --right;\n            }\n        }\n        return s;\n    }\n};","title":"Reverse Vowels of a String","url":"/submissions/detail/1098055331/","lang_name":"C++","time":"2 months, 3 weeks","timestamp":1699896295,"status":10,"runtime":"6 ms","is_pending":"Not Pending","memory":"7.9 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
               ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U';
    }

    string reverseVowels(string s) {
        unsigned long length{s.size()};
        unsigned long left{0}, right{length-1};
        while (left < right) {
            char chLeft{s[left]};
            char chRight{s[right]};
            if (!isVowel(chLeft)) {
                ++left;
            } else if (!isVowel(chRight)) {
                --right;
            } else {
                s[left] = chRight;
                s[right] = chLeft;
                ++left;
                --right;
            }
        }
        return s;
    }
};
