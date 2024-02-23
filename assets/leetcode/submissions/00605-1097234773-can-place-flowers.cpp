// Submission title: Can Place Flowers
// Submission url  : https://leetcode.com/problems/can-place-flowers/description/
// Submission url  : https://leetcode.com/submissions/detail/1097234773/"

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int curZeros = flowerbed[0] == 0 ? 2 : 0;
        int length = flowerbed.size();
        int ans = 0;
        for (int i = 1; i < length; ++i) {
            if (flowerbed[i] == 0) {
                curZeros += 1;
                continue;
            }
            ans += (curZeros - 1) / 2;
            curZeros = 0;
            if (ans >= n) {
                return true;
            }
        }
        ans += curZeros / 2;
        return ans >= n;
    }
};
