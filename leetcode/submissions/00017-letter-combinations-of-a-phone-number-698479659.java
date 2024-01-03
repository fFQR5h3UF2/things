// Submission title: for Letter Combinations of a Phone Number
// Submission url  : https://leetcode.com/submissions/detail/698479659/
// Submission json : {"id": 698479659, "status_display": "Accepted", "lang": "java", "question_id": 17, "title_slug": "letter-combinations-of-a-phone-number", "code": "class Solution {\n    public List<String> letterCombinations(String digits) {\n        if(digits.length() == 0){\n            List<String> result = new ArrayList<>();\n            return result;\n        }\n        List<String> res = combine(digits); \n        return res;\n    }\n    \n    public List<String> combine(String digit){\n        if(digit.length() == 0 ){\n            List<String> result = new ArrayList<>();\n            result.add(\"\");\n            return result;\n        }\n        \n        String[] codes = {\"\",\"\",\"abc\",\"def\",\"ghi\",\"jkl\",\"mno\",\"pqrs\",\"tuv\",\"wxyz\"};\n        \n        char c = digit.charAt(0);\n        \n        String  digits_left = digit.substring(1);\n        \n        List<String> res = combine(digits_left);\n        \n        List<String> result = new ArrayList<>();\n        \n        String code_for_current_digit = codes[c-'0'];\n        \n        for(int i=0;i<code_for_current_digit.length();i++){\n            char code_char = code_for_current_digit.charAt(i);\n            \n            if(!res.isEmpty()){\n                for(String s : res){\n                    result.add(code_char + s);\n                }    \n            }\n            else{\n                res.add(String.valueOf(code_char));\n            }\n            \n        }\n        \n        \n        return result;\n    }\n}", "title": "Letter Combinations of a Phone Number", "url": "/submissions/detail/698479659/", "lang_name": "Java", "time": "1\u00a0year, 8\u00a0months", "timestamp": 1652415550, "status": 10, "runtime": "8 ms", "is_pending": "Not Pending", "memory": "42.8 MB", "compare_result": "1111111111111111111111111", "has_notes": false, "flag_type": 1}

com.shishifubing.dotfiles.submissions

class Solution {
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0){
            List<String> result = new ArrayList<>();
            return result;
        }
        List<String> res = combine(digits);
        return res;
    }

    public List<String> combine(String digit){
        if(digit.length() == 0 ){
            List<String> result = new ArrayList<>();
            result.add("");
            return result;
        }

        String[] codes = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

        char c = digit.charAt(0);

        String  digits_left = digit.substring(1);

        List<String> res = combine(digits_left);

        List<String> result = new ArrayList<>();

        String code_for_current_digit = codes[c-'0'];

        for(int i=0;i<code_for_current_digit.length();i++){
            char code_char = code_for_current_digit.charAt(i);

            if(!res.isEmpty()){
                for(String s : res){
                    result.add(code_char + s);
                }
            }
            else{
                res.add(String.valueOf(code_char));
            }

        }


        return result;
    }
}