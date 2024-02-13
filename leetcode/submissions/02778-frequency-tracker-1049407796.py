# Submission title: Frequency Tracker
# Submission url  : https://leetcode.com/problems/frequency-tracker/description/
# Submission url  : https://leetcode.com/submissions/detail/1049407796/
# Submission json : {"id":1049407796,"status_display":"Accepted","lang":"python3","question_id":2778,"title_slug":"frequency-tracker","code":"class FrequencyTracker:\n\n    def __init__(self):\n        self._num_freq = defaultdict(int)\n        self._freq_nums = defaultdict(set)    \n\n    def add(self, number: int) -> None:\n        cur_freq = self._num_freq[number]\n        self._num_freq[number] = cur_freq + 1\n        self._freq_nums[cur_freq].discard(number)\n        self._freq_nums[cur_freq + 1].add(number)\n\n    def deleteOne(self, number: int) -> None:\n        cur_freq = self._num_freq[number]\n        if cur_freq == 0:\n            return    \n        self._num_freq[number] = cur_freq - 1 \n        self._freq_nums[cur_freq].discard(number)\n        if cur_freq != 1:\n            self._freq_nums[cur_freq - 1].add(number)\n\n    def hasFrequency(self, frequency: int) -> bool:\n        return len(self._freq_nums[frequency]) != 0\n\n\n# Your FrequencyTracker object will be instantiated and called as such:\n# obj = FrequencyTracker()\n# obj.add(number)\n# obj.deleteOne(number)\n# param_3 = obj.hasFrequency(frequency)","title":"Frequency Tracker","url":"/submissions/detail/1049407796/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694707334,"status":10,"runtime":"536 ms","is_pending":"Not Pending","memory":"80.1 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class FrequencyTracker:

    def __init__(self):
        self._num_freq = defaultdict(int)
        self._freq_nums = defaultdict(set)

    def add(self, number: int) -> None:
        cur_freq = self._num_freq[number]
        self._num_freq[number] = cur_freq + 1
        self._freq_nums[cur_freq].discard(number)
        self._freq_nums[cur_freq + 1].add(number)

    def deleteOne(self, number: int) -> None:
        cur_freq = self._num_freq[number]
        if cur_freq == 0:
            return
        self._num_freq[number] = cur_freq - 1
        self._freq_nums[cur_freq].discard(number)
        if cur_freq != 1:
            self._freq_nums[cur_freq - 1].add(number)

    def hasFrequency(self, frequency: int) -> bool:
        return len(self._freq_nums[frequency]) != 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
