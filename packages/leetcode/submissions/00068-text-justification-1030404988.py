# Submission title: for Text Justification
# Submission url  : https://leetcode.com/submissions/detail/1030404988/
# Submission json : {"id": 1030404988, "status_display": "Accepted", "lang": "python3", "question_id": 68, "title_slug": "text-justification", "code": "class Solution:\n    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:\n        words_count = len(words)\n        \n        def get_line(word_idx: int) -> Tuple[List[str], int]:\n            line = []\n            line_length = 0\n\n            for i in range(word_idx, words_count):\n                word = words[i]\n                word_length = len(word)\n                if line_length + word_length > maxWidth:\n                    break\n\n                line.append(word)\n                line_length += word_length + 1 \n\n            return line, line_length\n        \n        def create_line(line: List[str], line_length: int, word_idx: int) -> str:\n            base_length = line_length - 1\n            extra_spaces = maxWidth - base_length\n\n            if len(line) == 1 or word_idx == words_count:\n                return \" \".join(line) + \" \" * extra_spaces\n\n            word_count = len(line) - 1\n            spaces_per_word = extra_spaces // word_count\n            needs_extra_space = extra_spaces % word_count\n\n            for j in range(needs_extra_space):\n                line[j] += \" \"\n\n            for j in range(word_count):\n                line[j] += \" \" * spaces_per_word\n\n            return \" \".join(line)\n\n        result = []\n        i = 0\n        while i < words_count:\n            line, line_length = get_line(i)\n            i += len(line)\n            result.append(create_line(line, line_length, i))\n\n        return result", "title": "Text Justification", "url": "/submissions/detail/1030404988/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692873941, "status": 10, "runtime": "38 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_count = len(words)

        def get_line(word_idx: int) -> Tuple[List[str], int]:
            line = []
            line_length = 0

            for i in range(word_idx, words_count):
                word = words[i]
                word_length = len(word)
                if line_length + word_length > maxWidth:
                    break

                line.append(word)
                line_length += word_length + 1

            return line, line_length

        def create_line(line: List[str], line_length: int, word_idx: int) -> str:
            base_length = line_length - 1
            extra_spaces = maxWidth - base_length

            if len(line) == 1 or word_idx == words_count:
                return " ".join(line) + " " * extra_spaces

            word_count = len(line) - 1
            spaces_per_word = extra_spaces // word_count
            needs_extra_space = extra_spaces % word_count

            for j in range(needs_extra_space):
                line[j] += " "

            for j in range(word_count):
                line[j] += " " * spaces_per_word

            return " ".join(line)

        result = []
        i = 0
        while i < words_count:
            line, line_length = get_line(i)
            i += len(line)
            result.append(create_line(line, line_length, i))

        return result
