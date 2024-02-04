// Submission for Maximum Element After Decreasing and Rearranging
// Submission url: https://leetcode.com/submissions/detail/1099355567/



class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        auto length{arr.size()};
        int prev{1};
        for (int i = 1; i < length; ++i) {
            int num{arr[i]};
            int diff{std::abs(num - prev)};
            if (diff == 0) {
                continue;
            }
            if (diff == 1) {
                prev = num;
                continue;
            }
            if (i + 1 == length || arr[i+1] != num) {
                ++prev;
            }
        }
        return prev;
    }
};
