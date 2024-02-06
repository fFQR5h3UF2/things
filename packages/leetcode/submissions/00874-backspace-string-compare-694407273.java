// Submission title: for Backspace String Compare
// Submission url  : https://leetcode.com/submissions/detail/694407273/
// Submission json : {"id": 694407273, "status_display": "Accepted", "lang": "java", "question_id": 874, "title_slug": "backspace-string-compare", "code": "class Solution {\n    public boolean backspaceCompare(String S, String T) {\n        return build(S).equals(build(T));\n    }\n\n    public String build(String S) {\n        Stack<Character> ans = new Stack();\n        for (char c: S.toCharArray()) {\n            if (c != '#')\n                ans.push(c);\n            else if (!ans.empty())\n                ans.pop();\n        }\n        return String.valueOf(ans);\n    }\n}", "title": "Backspace String Compare", "url": "/submissions/detail/694407273/", "lang_name": "Java", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651856578, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "40.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

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
