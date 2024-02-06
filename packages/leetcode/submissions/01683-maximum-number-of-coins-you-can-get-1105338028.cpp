// Submission title: for Maximum Number of Coins You Can Get
// Submission url  : https://leetcode.com/submissions/detail/1105338028/
// Submission json : {"id": 1105338028, "status_display": "Accepted", "lang": "cpp", "question_id": 1683, "title_slug": "maximum-number-of-coins-you-can-get", "code": "class Solution {\npublic:\n    int maxCoins(vector<int>& piles) {\n        std::sort(piles.begin(), piles.end());\n        size_t length {piles.size()};\n        size_t picks {length / 3};\n        int count {};\n        for (size_t i {length - 2}; picks > 0; i -= 2, --picks) {\n            count += piles[i];\n        }\n        return count;\n    }\n};", "title": "Maximum Number of Coins You Can Get", "url": "/submissions/detail/1105338028/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1700813257, "status": 10, "runtime": "92 ms", "is_pending": "Not Pending", "memory": "53.8 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
