// Submission title: for Maximum Element After Decreasing and Rearranging
// Submission url  : https://leetcode.com/submissions/detail/1099356606/
// Submission json : {"id": 1099356606, "status_display": "Accepted", "lang": "cpp", "question_id": 1956, "title_slug": "maximum-element-after-decreasing-and-rearranging", "code": "class Solution {\npublic:\n    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {\n        std::sort(arr.begin(), arr.end());\n        auto length{arr.size()};\n        int prev{1};\n        for (int i = 1; i < length; ++i) {\n            if (arr[i] == prev) {\n                continue;\n            }\n            ++prev;\n        }\n        return prev;\n    }\n};", "title": "Maximum Element After Decreasing and Rearranging", "url": "/submissions/detail/1099356606/", "lang_name": "C++", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1700050650, "status": 10, "runtime": "76 ms", "is_pending": "Not Pending", "memory": "51.6 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& arr) {
        std::sort(arr.begin(), arr.end());
        auto length{arr.size()};
        int prev{1};
        for (int i = 1; i < length; ++i) {
            if (arr[i] == prev) {
                continue;
            }
            ++prev;
        }
        return prev;
    }
};
