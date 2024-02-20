// Submission title: Kids With the Greatest Number of Candies
// Submission url  : https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
// Submission url  : https://leetcode.com/submissions/detail/1105481191/"

class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        size_t length {candies.size()};
        std::vector<bool> ans {};
        ans.resize(length);
        const int maxCandy {*std::max_element(candies.begin(), candies.end())};
        for (size_t i = 0; i < length; ++i) {
            ans[i] = (candies[i] + extraCandies) >= maxCandy;
        }
        return ans;
    }
};
