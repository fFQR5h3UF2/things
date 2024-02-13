# Submission title: Design Parking System
# Submission url  : https://leetcode.com/problems/design-parking-system/description/
# Submission url  : https://leetcode.com/submissions/detail/1047430740/
# Submission json : {"id":1047430740,"status_display":"Accepted","lang":"python3","question_id":1708,"title_slug":"design-parking-system","code":"class ParkingSystem:\n\n    def __init__(self, big: int, medium: int, small: int):\n        self._slots = [big, medium, small]\n\n    def addCar(self, carType: int) -> bool:\n        if self._slots[carType-1] == 0:\n            return False\n        self._slots[carType-1] -= 1\n        return True\n\n\n# Your ParkingSystem object will be instantiated and called as such:\n# obj = ParkingSystem(big, medium, small)\n# param_1 = obj.addCar(carType)","title":"Design Parking System","url":"/submissions/detail/1047430740/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694521436,"status":10,"runtime":"125 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self._slots[carType - 1] == 0:
            return False
        self._slots[carType - 1] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
