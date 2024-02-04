// Submission for Largest 3-Same-Digit Number in String
// Submission url: https://leetcode.com/submissions/detail/1112022298/



class Solution {
public:
    string largestGoodInteger(string num) {
        int cur {-1};
        int max {-1};
        int count {0};
        for (const char& ch : num) {
            int i {ch - '0'};
            if (i == cur) {
                ++count;
            } else {
                cur = i;
                count = 1;
            }
            if (count == 3) {
                max = std::max(i, max);
            }
        }
        if (max == -1) {
            return "";
        }
        std::string ans {std::to_string(max)};
        return ans + ans + ans;
    }
};
