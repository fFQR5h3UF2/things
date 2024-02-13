// Submission title: Count of Matches in Tournament
// Submission url  : https://leetcode.com/problems/count-of-matches-in-tournament/description/
// Submission url  : https://leetcode.com/submissions/detail/1112898278/
// Submission json : {"id":1112898278,"status_display":"Accepted","lang":"cpp","question_id":1806,"title_slug":"count-of-matches-in-tournament","code":"class Solution {\npublic:\n    int numberOfMatches(int n) {\n        int ans = 0;\n        while (n > 1) {\n            if (n % 2 == 0) {\n                int matches {n / 2};\n                ans += matches;\n                n = matches;\n            } else {\n                int matches {(n - 1) / 2};\n                ans += matches;\n                n = matches + 1;\n            }\n        }\n        \n        return ans;\n    }\n};","title":"Count of Matches in Tournament","url":"/submissions/detail/1112898278/","lang_name":"C++","time":"2 months","timestamp":1701781944,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"6.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

class Solution {
public:
    int numberOfMatches(int n) {
        int ans = 0;
        while (n > 1) {
            if (n % 2 == 0) {
                int matches {n / 2};
                ans += matches;
                n = matches;
            } else {
                int matches {(n - 1) / 2};
                ans += matches;
                n = matches + 1;
            }
        }

        return ans;
    }
};
