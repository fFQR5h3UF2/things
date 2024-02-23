// Submission title: Backspace String Compare
// Submission url  : https://leetcode.com/problems/backspace-string-compare/description/
// Submission url  : https://leetcode.com/submissions/detail/694407273/"
com.shishifubing.dotfiles.submissions
class Solution {
    public boolean backspaceCompare(String S, String T) {
        return build(S).equals(build(T));
    }

    public String build(String S) {
        Stack<Character> ans = new Stack();
        for (char c: S.toCharArray()) {
            if (c != '#')
                ans.push(c);
            else if (!ans.empty())
                ans.pop();
        }
        return String.valueOf(ans);
    }
}
