// Submission title: Maximum Number of Coins You Can Get
// Submission url  : https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/"
// Submission url  : https://leetcode.com/submissions/detail/1105338028/"

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        std::sort(piles.begin(), piles.end());
        size_t length {piles.size()};
        size_t picks {length / 3};
        int count {};
        for (size_t i {length - 2}; picks > 0; i -= 2, --picks) {
            count += piles[i];
        }
        return count;
    }
};
