// Submission for Valid Parentheses
// Submission url: https://leetcode.com/submissions/detail/1096532762/



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
                    if (stack.back() != '(') {
                        return false;
                    }
                    stack.pop_back();
                    break;
                case '}':
                    if (stack.back() != '{') {
                        return false;
                    }
                    stack.pop_back();
                    break;
                case ']':
                    if (stack.back() != '[') {
                        return false;
                    }
                    stack.pop_back();
                    break;
            }
        }
        return true;
    }
};
