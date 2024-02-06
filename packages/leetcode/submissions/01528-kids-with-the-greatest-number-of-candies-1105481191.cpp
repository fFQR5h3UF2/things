// Submission title: for Kids With the Greatest Number of Candies
// Submission url  : https://leetcode.com/submissions/detail/1105481191/
// Submission json : {"id": 1105481191, "status_display": "Accepted", "lang": "cpp", "question_id": 1528, "title_slug": "kids-with-the-greatest-number-of-candies", "code": "class Solution {\npublic:\n    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {\n        size_t length {candies.size()};        \n        std::vector<bool> ans {};\n        ans.resize(length);\n        const int maxCandy {*std::max_element(candies.begin(), candies.end())};\n        for (size_t i = 0; i < length; ++i) {\n            ans[i] = (candies[i] + extraCandies) >= maxCandy;\n        }\n        return ans;\n    }\n};", "title": "Kids With the Greatest Number of Candies", "url": "/submissions/detail/1105481191/", "lang_name": "C++", "time": "2\u00a0months, 1\u00a0week", "timestamp": 1700833772, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "9.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}



class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        size_t length {candies.size()};
        std::vector<bool> ans {};
        ans.resize(length);
        const int maxCandy {*std::max_element(candies.begin(), candies.end())};
        for (size_t i = 0; i < length; ++i) {
            ans[i] = (candies[i] + extraCandies) >= maxCandy;
        }
        return ans;
    }
};
