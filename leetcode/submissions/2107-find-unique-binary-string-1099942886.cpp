// Submission for Find Unique Binary String
// Submission url: https://leetcode.com/submissions/detail/1099942886/



class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        string ans;
        auto length{nums.size()};
        auto stringLength{nums[0].size()};
        for (int j = 0; j < stringLength; ++j) {
            bool gotZero{false}, gotOne{false};
            for (int i = 0; i < length; ++i) {
                if (nums[i][j] == '0') {
                    gotZero = true;
                } else {
                    gotOne = true;
                }
                if (gotZero && gotOne) {
                    break;
                }
            }
            if (gotZero && gotOne) {
                ans += '1';
            } else if (!gotZero) {
                ans += '0';
            } else {
                ans += '1';
            }
        }
        return ans;
    }
};
