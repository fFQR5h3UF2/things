// Submission for Kids With the Greatest Number of Candies
// Submission url: https://leetcode.com/submissions/detail/1105479213/



class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        size_t length {candies.size()};
        std::vector<bool> ans {};
        ans.resize(length);
        const int maxCandy {std::max(candies)};
        for (size_t i = 0; i < length; ++i) {
            ans[i] = candies[i] == maxCandy;
        }
        return ans;
    }
};
