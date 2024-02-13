// Submission title: Flatten Nested List Iterator
// Submission url  : https://leetcode.com/problems/flatten-nested-list-iterator/description/
// Submission url  : https://leetcode.com/submissions/detail/695536827/
// Submission json : {"id":695536827,"status_display":"Accepted","lang":"java","question_id":341,"title_slug":"flatten-nested-list-iterator","code":"public class NestedIterator implements Iterator<Integer> {\n\n    private List<Integer> integerList = new ArrayList<>();\n    private int index = 0;\n    public NestedIterator(List<NestedInteger> nestedList) {\n        for (NestedInteger nestedInteger : nestedList) {\n            flatten(nestedInteger);\n        }\n    }\n    \n    private void flatten(NestedInteger nested) {\n        if (nested.isInteger()) \n            integerList.add(nested.getInteger());\n        else \n            for (NestedInteger nestedFromList : nested.getList()) {\n                flatten(nestedFromList);\n        }\n    }\n\n    @Override\n    public boolean hasNext() {\n        return index < integerList.size();\n    }\n\n    @Override\n    public Integer next() {\n        return integerList.get(index++);\n    }\n}\n","title":"Flatten Nested List Iterator","url":"/submissions/detail/695536827/","lang_name":"Java","time":"1 year, 9 months","timestamp":1652020040,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"44.3 MB","compare_result":"1111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
com.shishifubing.dotfiles.submissions
public class NestedIterator implements Iterator<Integer> {

    private List<Integer> integerList = new ArrayList<>();
    private int index = 0;
    public NestedIterator(List<NestedInteger> nestedList) {
        for (NestedInteger nestedInteger : nestedList) {
            flatten(nestedInteger);
        }
    }

    private void flatten(NestedInteger nested) {
        if (nested.isInteger())
            integerList.add(nested.getInteger());
        else
            for (NestedInteger nestedFromList : nested.getList()) {
                flatten(nestedFromList);
        }
    }

    @Override
    public boolean hasNext() {
        return index < integerList.size();
    }

    @Override
    public Integer next() {
        return integerList.get(index++);
    }
}
