// Submission title: Find Words That Can Be Formed by Characters
// Submission url  : https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
// Submission url  : https://leetcode.com/submissions/detail/1111055227/"

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        std::vector<int> count {};
        int ans {};
        count.resize(26);
        for (const char& ch : chars) {
            ++count[ch - 'a'];
        }
        for (const string& word : words) {
            std::vector<int> wordCount {};
            wordCount.resize(26);
            bool failure {false};
            for (const char& ch : word) {
                int i {ch - 'a'};
                int cur {++wordCount[i]};
                if (cur > count[i]) {
                    failure = true;
                    break;
                }
            }
            if (!failure) {
                ans += word.length();
            }
        }
        return ans;
    }
};
