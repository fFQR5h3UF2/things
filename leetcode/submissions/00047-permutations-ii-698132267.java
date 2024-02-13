// Submission title: Permutations II
// Submission url  : https://leetcode.com/problems/permutations-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/698132267/
// Submission json : {"id":698132267,"status_display":"Accepted","lang":"java","question_id":47,"title_slug":"permutations-ii","code":"class Solution {\npublic List<List<Integer>> permuteUnique(int[] nums) {\n        List<List<Integer>> permutations = new ArrayList<>();\n        Arrays.sort(nums);\n        backtracking(permutations, new ArrayList<>(), nums, new boolean[nums.length]);\n        return permutations;\n    }\n\n    private void backtracking(List<List<Integer>> permutations, List<Integer> current, int[] nums, boolean[] used) {\n        if (current.size() == nums.length)\n            permutations.add(new ArrayList<>(current));\n        else {\n            for (int i = 0; i < nums.length; i++) {\n                if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) continue;\n                current.add(nums[i]);\n                used[i] = true;\n                backtracking(permutations, current, nums, used);\n                used[i] = false;\n                current.remove(current.size() - 1);\n            }\n        }\n    }\n}","title":"Permutations II","url":"/submissions/detail/698132267/","lang_name":"Java","time":"1 year, 8 months","timestamp":1652367933,"status":10,"runtime":"4 ms","is_pending":"Not Pending","memory":"48.2 MB","compare_result":"111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
class Solution {
public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> permutations = new ArrayList<>();
        Arrays.sort(nums);
        backtracking(permutations, new ArrayList<>(), nums, new boolean[nums.length]);
        return permutations;
    }

    private void backtracking(List<List<Integer>> permutations, List<Integer> current, int[] nums, boolean[] used) {
        if (current.size() == nums.length)
            permutations.add(new ArrayList<>(current));
        else {
            for (int i = 0; i < nums.length; i++) {
                if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) continue;
                current.add(nums[i]);
                used[i] = true;
                backtracking(permutations, current, nums, used);
                used[i] = false;
                current.remove(current.size() - 1);
            }
        }
    }
}
