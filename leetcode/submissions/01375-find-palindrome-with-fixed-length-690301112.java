// Submission title: Find Palindrome With Fixed Length
// Submission url  : https://leetcode.com/problems/find-palindrome-with-fixed-length/description/
// Submission url  : https://leetcode.com/submissions/detail/690301112/
// Submission json : {"id":690301112,"status_display":"Accepted","lang":"java","question_id":1375,"title_slug":"find-palindrome-with-fixed-length","code":"class Solution {\n    public long[] kthPalindrome(int[] queries, int intLength) {\n        long[] res= new long[queries.length];\n        for(int i=0;i<queries.length;i++){\n            res[i]=nthPalindrome(queries[i],intLength);\n        }\n        return res;\n    }\n    public long nthPalindrome(int nth, int kdigit)\n    {\n    long temp = (kdigit & 1)!=0 ? (kdigit / 2) : (kdigit/2 - 1);\n    long palindrome = (long)Math.pow(10, temp);\n    palindrome += nth - 1;\n    long res1=palindrome;\n    if ((kdigit & 1)>0)\n        palindrome /= 10;\n    while (palindrome>0)\n    {\n        res1=res1*10+(palindrome % 10);\n        palindrome /= 10;\n    }\n    String g=\"\";\n    g+=res1;\n    if(g.length()!=kdigit)\n        return -1;\n    return res1;\n}\n}","title":"Find Palindrome With Fixed Length","url":"/submissions/detail/690301112/","lang_name":"Java","time":"1 year, 9 months","timestamp":1651332888,"status":10,"runtime":"73 ms","is_pending":"Not Pending","memory":"52.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
    public long[] kthPalindrome(int[] queries, int intLength) {
        long[] res= new long[queries.length];
        for(int i=0;i<queries.length;i++){
            res[i]=nthPalindrome(queries[i],intLength);
        }
        return res;
    }
    public long nthPalindrome(int nth, int kdigit)
    {
    long temp = (kdigit & 1)!=0 ? (kdigit / 2) : (kdigit/2 - 1);
    long palindrome = (long)Math.pow(10, temp);
    palindrome += nth - 1;
    long res1=palindrome;
    if ((kdigit & 1)>0)
        palindrome /= 10;
    while (palindrome>0)
    {
        res1=res1*10+(palindrome % 10);
        palindrome /= 10;
    }
    String g="";
    g+=res1;
    if(g.length()!=kdigit)
        return -1;
    return res1;
}
}
