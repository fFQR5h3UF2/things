// Submission title: Count Sorted Vowel Strings
// Submission url  : https://leetcode.com/problems/count-sorted-vowel-strings/description/
// Submission url  : https://leetcode.com/submissions/detail/697487494/
// Submission json : {"id":697487494,"status_display":"Accepted","lang":"java","question_id":1761,"title_slug":"count-sorted-vowel-strings","code":"class Solution {\n    public int countVowelStrings(int n) {\n        int a,e,i,o,u;\n        a = e = i = o = u = 1;\n        \n        for(int t = 1; t < n; t++){\n            \n            a = a + e + i + o + u;\n            e = e + i + o + u;\n            i = i + o + u;\n            o = o + u;\n            u = u;\n        }\n        return a + e + i + o + u;\n    }\n}","title":"Count Sorted Vowel Strings","url":"/submissions/detail/697487494/","lang_name":"Java","time":"1 year, 8 months","timestamp":1652281386,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"40.5 MB","compare_result":"11111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
    public int countVowelStrings(int n) {
        int a,e,i,o,u;
        a = e = i = o = u = 1;

        for(int t = 1; t < n; t++){

            a = a + e + i + o + u;
            e = e + i + o + u;
            i = i + o + u;
            o = o + u;
            u = u;
        }
        return a + e + i + o + u;
    }
}
