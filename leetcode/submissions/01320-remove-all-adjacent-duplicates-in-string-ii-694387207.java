// Submission title: Remove All Adjacent Duplicates in String II
// Submission url  : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/694387207/
// Submission json : {"id":694387207,"status_display":"Accepted","lang":"java","question_id":1320,"title_slug":"remove-all-adjacent-duplicates-in-string-ii","code":"class Solution {\n    public String removeDuplicates(String s, int k) {\n        Stack<int []> Master = new Stack<>();\n        \n        for(char ch : s.toCharArray()){\n            if(!Master.isEmpty() && Master.peek()[0] == ch){\n                Master.peek()[1]++;\n            }\n            else Master.push(new int[]{ch, 1});\n            if(Master.peek()[1] == k) Master.pop();\n        }\n        StringBuilder sb = new StringBuilder();\n        while(!Master.isEmpty()){\n            int top[] = Master.pop();\n            while(top[1] --> 0)\n                sb.append((char)top[0]);\n        }\n        return sb.reverse().toString();\n    }\n}","title":"Remove All Adjacent Duplicates in String II","url":"/submissions/detail/694387207/","lang_name":"Java","time":"1 year, 9 months","timestamp":1651854299,"status":10,"runtime":"84 ms","is_pending":"Not Pending","memory":"50 MB","compare_result":"11111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<int []> Master = new Stack<>();

        for(char ch : s.toCharArray()){
            if(!Master.isEmpty() && Master.peek()[0] == ch){
                Master.peek()[1]++;
            }
            else Master.push(new int[]{ch, 1});
            if(Master.peek()[1] == k) Master.pop();
        }
        StringBuilder sb = new StringBuilder();
        while(!Master.isEmpty()){
            int top[] = Master.pop();
            while(top[1] --> 0)
                sb.append((char)top[0]);
        }
        return sb.reverse().toString();
    }
}
