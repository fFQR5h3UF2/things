# Submission for Design Parking System
# Submission url: https://leetcode.com/submissions/detail/1047430740/


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
