// Submission title: Largest Odd Number in String
// Submission url  : https://leetcode.com/problems/largest-odd-number-in-string/description/
// Submission url  : https://leetcode.com/submissions/detail/1114478635/"

class Solution {
public:
    string largestOddNumber(string num) {
        size_t length {num.size()};
        for (int i = length - 1; i >= 0; --i) {
            if ((num[i] - '0') % 2 != 0) {
                return num.substr(0, i + 1);
            }
        }
        return "";
    }
};
