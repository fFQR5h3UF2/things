# Submission title: Design Underground System
# Submission url  : https://leetcode.com/problems/design-underground-system/description/
# Submission url  : https://leetcode.com/submissions/detail/1051136998/
# Submission json : {"id":1051136998,"status_display":"Accepted","lang":"python3","question_id":1512,"title_slug":"design-underground-system","code":"class UndergroundSystem:\n\n    def __init__(self):\n        self.from_to = defaultdict(lambda: defaultdict(list))\n        self.in_transit = {}\n\n    def checkIn(self, id: int, stationName: str, t: int) -> None:\n        self.in_transit[id] = (stationName, t)\n\n    def checkOut(self, id: int, stationName: str, t: int) -> None:\n        station_from, time_from = self.in_transit.pop(id)\n        self.from_to[station_from][stationName].append(t - time_from)\n\n    def getAverageTime(self, startStation: str, endStation: str) -> float:\n        times = self.from_to[startStation][endStation]\n        return sum(times) / len(times)\n\n\n# Your UndergroundSystem object will be instantiated and called as such:\n# obj = UndergroundSystem()\n# obj.checkIn(id,stationName,t)\n# obj.checkOut(id,stationName,t)\n# param_3 = obj.getAverageTime(startStation,endStation)","title":"Design Underground System","url":"/submissions/detail/1051136998/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1694886274,"status":10,"runtime":"241 ms","is_pending":"Not Pending","memory":"26.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class UndergroundSystem:

    def __init__(self):
        self.from_to = defaultdict(lambda: defaultdict(list))
        self.in_transit = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_transit[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_from, time_from = self.in_transit.pop(id)
        self.from_to[station_from][stationName].append(t - time_from)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.from_to[startStation][endStation]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
