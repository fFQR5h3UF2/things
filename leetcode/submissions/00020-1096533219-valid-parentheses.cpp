// Submission title: Valid Parentheses
// Submission url  : https://leetcode.com/problems/valid-parentheses/description/"
// Submission url  : https://leetcode.com/submissions/detail/1096533219/"

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
