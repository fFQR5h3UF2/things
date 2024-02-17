// Submission title: Greatest Common Divisor of Strings
// Submission url  : https://leetcode.com/problems/greatest-common-divisor-of-strings/description/"
// Submission url  : https://leetcode.com/submissions/detail/1105475590/"

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 == str2 + str1) {
            return str1.substr(0, std::gcd(str1.size(), str2.size()));
        }
        return "";
    }
};
