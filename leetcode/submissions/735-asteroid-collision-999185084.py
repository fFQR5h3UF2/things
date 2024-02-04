# Submission for Asteroid Collision
# Submission url: https://leetcode.com/submissions/detail/999185084/


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        length = len(asteroids)

        if length < 2:
            return asteroids

        for i in reversed(range(0, length - 1)):
            asteroid, asteroid_prev = asteroids[i], asteroids[i + 1]

            if asteroid_prev > 0:
                continue

            mass, mass_prev = abs(asteroid), abs(asteroid_prev)
            if mass == mass_prev:
                asteroids.pop(i + 1)
                asteroids.pop(i)
            elif mass_prev > mass:
                asteroids[i] = asteroid_prev
                asteroids.pop(i + 1)
            else:
                asteroids.pop(i + 1)

        return asteroids
