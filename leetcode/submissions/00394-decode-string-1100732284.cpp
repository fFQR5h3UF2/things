// Submission title: Decode String
// Submission url  : https://leetcode.com/problems/decode-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1100732284/
// Submission json : {"id":1100732284,"status_display":"Accepted","lang":"cpp","question_id":394,"title_slug":"decode-string","code":"class Solution {\npublic:\n    string decodeString(string s) {\n        return std::get<1>(decode(0, s));\n    }\n    \n    std::tuple<int, string> decode(int pos, string s) {\n        int num {0};\n        string word {\"\"};\n        unsigned long length {s.size()};\n        for(; pos < length; ++pos) {\n            char c = s[pos];\n            if(c == '[') {\n                auto [newPos, repeat] {decode(++pos, s)};\n                for(; num > 0; --num) {\n                    word += repeat;\n                }\n                pos = newPos;\n            } else if (c >= '0' && c <='9') {\n                num = num * 10 + (c - '0');\n            } else if (c == ']') {\n                return {pos, word};\n            } else {\n                word += c;\n            }\n        }\n        return {pos, word};\n    }\n};","title":"Decode String","url":"/submissions/detail/1100732284/","lang_name":"C++","time":"2 months, 2 weeks","timestamp":1700219135,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"7.1 MB","compare_result":"1111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    string decodeString(string s) {
        return std::get<1>(decode(0, s));
    }

    std::tuple<int, string> decode(int pos, string s) {
        int num {0};
        string word {""};
        unsigned long length {s.size()};
        for(; pos < length; ++pos) {
            char c = s[pos];
            if(c == '[') {
                auto [newPos, repeat] {decode(++pos, s)};
                for(; num > 0; --num) {
                    word += repeat;
                }
                pos = newPos;
            } else if (c >= '0' && c <='9') {
                num = num * 10 + (c - '0');
            } else if (c == ']') {
                return {pos, word};
            } else {
                word += c;
            }
        }
        return {pos, word};
    }
};
