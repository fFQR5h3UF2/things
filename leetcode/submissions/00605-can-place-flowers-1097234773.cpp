// Submission title: for Can Place Flowers
// Submission url  : https://leetcode.com/submissions/detail/1097234773/
// Submission json : {"id": 1097234773, "status_display": "Accepted", "lang": "cpp", "question_id": 605, "title_slug": "can-place-flowers", "code": "class Solution {\npublic:\n    bool canPlaceFlowers(vector<int>& flowerbed, int n) {\n        int curZeros = flowerbed[0] == 0 ? 2 : 0;\n        int length = flowerbed.size();\n        int ans = 0;\n        for (int i = 1; i < length; ++i) { \n            if (flowerbed[i] == 0) {\n                curZeros += 1;\n                continue;\n            }\n            ans += (curZeros - 1) / 2;\n            curZeros = 0;\n            if (ans >= n) {\n                return true;\n            }\n        }\n        ans += curZeros / 2;\n        return ans >= n;\n    }\n};", "title": "Can Place Flowers", "url": "/submissions/detail/1097234773/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699793035, "status": 10, "runtime": "9 ms", "is_pending": "Not Pending", "memory": "20.7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



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
