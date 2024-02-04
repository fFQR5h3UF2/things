// Submission for Reverse Vowels of a String
// Submission url: https://leetcode.com/submissions/detail/1098054796/



class Solution {
public:
    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }

    string reverseVowels(string s) {
        unsigned long length{s.size()};
        unsigned long left{0}, right{length-1};
        while (left < right) {
            char chLeft{s[left]};
            char chRight{s[right]};
            if (!isVowel(chLeft)) {
                ++left;
            } else if (!isVowel(chRight)) {
                --right;
            } else {
                s[left] = chRight;
                s[right] = chLeft;
                ++left;
                --right;
            }
        }
        return s;
    }
};
