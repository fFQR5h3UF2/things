# Submission for Asteroid Collision
# Submission url: https://leetcode.com/submissions/detail/999177739/


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
                asteroids.pop()
            elif mass_prev > mass:
                asteroids[i] = asteroid_prev
            asteroids.pop()

        return asteroids
