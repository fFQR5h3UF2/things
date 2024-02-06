// Submission title: for Valid Parentheses
// Submission url  : https://leetcode.com/submissions/detail/1096533219/
// Submission json : {"id": 1096533219, "status_display": "Accepted", "lang": "cpp", "question_id": 20, "title_slug": "valid-parentheses", "code": "class Solution {\npublic:\n    bool isValid(string s) {\n        std::vector<char> stack;\n        for (const auto& ch : s) {\n            switch (ch){\n                case '[':\n                case '{':\n                case '(':\n                    stack.push_back(ch);\n                    break;\n                case ')':\n                    if (stack.empty() || stack.back() != '(') {\n                        return false;\n                    }\n                    stack.pop_back();\n                    break;\n                case '}':\n                    if (stack.empty() || stack.back() != '{') {\n                        return false;\n                    }\n                    stack.pop_back();\n                    break;\n                case ']':\n                    if (stack.empty() || stack.back() != '[') {\n                        return false;\n                    }\n                    stack.pop_back();\n                    break;\n            }\n        }\n        return stack.size() == 0;\n    }\n};", "title": "Valid Parentheses", "url": "/submissions/detail/1096533219/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699707178, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "6.8 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    bool isValid(string s) {
        std::vector<char> stack;
        for (const auto& ch : s) {
            switch (ch){
                case '[':
                case '{':
                case '(':
                    stack.push_back(ch);
                    break;
                case ')':
                    if (stack.empty() || stack.back() != '(') {
                        return false;
                    }
                    stack.pop_back();
                    break;
                case '}':
                    if (stack.empty() || stack.back() != '{') {
                        return false;
                    }
                    stack.pop_back();
                    break;
                case ']':
                    if (stack.empty() || stack.back() != '[') {
                        return false;
                    }
                    stack.pop_back();
                    break;
            }
        }
        return stack.size() == 0;
    }
};
