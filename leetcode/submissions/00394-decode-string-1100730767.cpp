// Submission title: for Decode String
// Submission url  : https://leetcode.com/submissions/detail/1100730767/
// Submission json : {"id": 1100730767, "status_display": "Accepted", "lang": "cpp", "question_id": 394, "title_slug": "decode-string", "code": "class Solution {\npublic:\n    string decodeString(string s) {\n        int pos = 0;\n        return decode(pos, s);\n    }\n    \n    string decode(int& pos, string s) {\n        int num {0};\n        string word {\"\"};\n        unsigned long length {s.size()};\n        for(; pos < length; ++pos) {\n            char c = s[pos];\n            if(c == '[') {\n                string repeat {decode(++pos, s)};\n                for(; num > 0; --num) {\n                    word += repeat;\n                }\n            } else if (c >= '0' && c <='9') {\n                num = num * 10 + (c - '0');\n            } else if (c == ']') {\n                return word;\n            } else {\n                word += c;\n            }\n        }\n        return word;\n    }\n};", "title": "Decode String", "url": "/submissions/detail/1100730767/", "lang_name": "C++", "time": "2\u00a0months, 2\u00a0weeks", "timestamp": 1700218925, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "6.8 MB", "compare_result": "1111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    string decodeString(string s) {
        int pos = 0;
        return decode(pos, s);
    }

    string decode(int& pos, string s) {
        int num {0};
        string word {""};
        unsigned long length {s.size()};
        for(; pos < length; ++pos) {
            char c = s[pos];
            if(c == '[') {
                string repeat {decode(++pos, s)};
                for(; num > 0; --num) {
                    word += repeat;
                }
            } else if (c >= '0' && c <='9') {
                num = num * 10 + (c - '0');
            } else if (c == ']') {
                return word;
            } else {
                word += c;
            }
        }
        return word;
    }
};
