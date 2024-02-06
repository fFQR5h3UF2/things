// Submission title: for Knight Dialer
// Submission url  : https://leetcode.com/submissions/detail/1107276458/
// Submission json : {"id": 1107276458, "status_display": "Accepted", "lang": "cpp", "question_id": 972, "title_slug": "knight-dialer", "code": "class Solution {\npublic:\n    vector<vector<int>> memo;\n    int n;\n    int MOD = 1e9 + 7;\n    vector<vector<int>> jumps = {\n        {4, 6},\n        {6, 8},\n        {7, 9},\n        {4, 8},\n        {3, 9, 0},\n        {},\n        {1, 7, 0},\n        {2, 6},\n        {1, 3},\n        {2, 4}\n    };\n    \n    int dp(int remain, int square) {\n        if (remain == 0) {\n            return 1;\n        }\n        \n        if (memo[remain][square] != 0) {\n            return memo[remain][square];\n        }\n        \n        int ans = 0;\n        for (int nextSquare : jumps[square]) {\n            ans = (ans + dp(remain - 1, nextSquare)) % MOD;\n        }\n        \n        memo[remain][square] = ans;\n        return ans;\n    }\n    \n    int knightDialer(int n) {\n        this->n = n;\n        memo = vector(n + 1, vector(10, 0));\n        int ans = 0;\n        for (int square = 0; square < 10; square++) {\n            ans = (ans + dp(n - 1, square)) % MOD;\n        }\n        \n        return ans;\n    }\n};", "title": "Knight Dialer", "url": "/submissions/detail/1107276458/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1701070332, "status": 10, "runtime": "160 ms", "is_pending": "Not Pending", "memory": "39.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    vector<vector<int>> memo;
    int n;
    int MOD = 1e9 + 7;
    vector<vector<int>> jumps = {
        {4, 6},
        {6, 8},
        {7, 9},
        {4, 8},
        {3, 9, 0},
        {},
        {1, 7, 0},
        {2, 6},
        {1, 3},
        {2, 4}
    };

    int dp(int remain, int square) {
        if (remain == 0) {
            return 1;
        }

        if (memo[remain][square] != 0) {
            return memo[remain][square];
        }

        int ans = 0;
        for (int nextSquare : jumps[square]) {
            ans = (ans + dp(remain - 1, nextSquare)) % MOD;
        }

        memo[remain][square] = ans;
        return ans;
    }

    int knightDialer(int n) {
        this->n = n;
        memo = vector(n + 1, vector(10, 0));
        int ans = 0;
        for (int square = 0; square < 10; square++) {
            ans = (ans + dp(n - 1, square)) % MOD;
        }

        return ans;
    }
};
