// Submission title: Count Nice Pairs in an Array
// Submission url  : https://leetcode.com/problems/count-nice-pairs-in-an-array/description/
// Submission url  : https://leetcode.com/submissions/detail/1103351460/"

class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        std::unordered_map<int, int> diffs{};
        int ans{};
        double mod{1e9 + 7};
        for (const int& num : nums) {
            int revNum{};
            int tempNum{num};
            while(tempNum) {
                revNum = (revNum * 10) + (tempNum % 10);
                tempNum /= 10;
            }
            int diff{num-revNum};
            if (diffs.contains(diff)) {
                ans = std::fmod(ans + diffs[diff], mod);
            }
            ++diffs[diff];
        }
        return ans;
    }

};
