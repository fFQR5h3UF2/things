# Submission title: for Design a Food Rating System
# Submission url  : https://leetcode.com/submissions/detail/1121678346/
# Submission json : {"id": 1121678346, "status_display": "Accepted", "lang": "python3", "question_id": 2429, "title_slug": "design-a-food-rating-system", "code": "class Food:\n    def __init__(self, food_rating, food_name):\n        # Store the food's rating.\n        self.food_rating = food_rating\n        # Store the food's name.\n        self.food_name = food_name\n\n    def __lt__(self, other):\n        # Overload the less than operator for comparison.\n        # If food ratings are the same, sort based on their name (lexicographically smaller name food will be on top).\n        if self.food_rating == other.food_rating:\n            return self.food_name < other.food_name\n        # Sort based on food rating (bigger rating food will be on top).\n        return self.food_rating > other.food_rating\n\nclass FoodRatings:\n    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):\n        # Map food with its rating.\n        self.food_rating_map = {}\n        # Map food with the cuisine it belongs to.\n        self.food_cuisine_map = {}\n        # Store all food of a cuisine in a priority queue (to sort them on ratings/name).\n        # Priority queue element -> Food: (food_rating, food_name)\n        self.cuisine_food_map = defaultdict(list)\n\n        for i in range(len(foods)):\n            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.\n            self.food_rating_map[foods[i]] = ratings[i]\n            self.food_cuisine_map[foods[i]] = cuisines[i]\n            # Insert the '(rating, name)' element into the current cuisine's priority queue.\n            heapq.heappush(self.cuisine_food_map[cuisines[i]], Food(ratings[i], foods[i]))\n\n    def changeRating(self, food: str, newRating: int) -> None:\n        # Update food's rating in 'food_rating' map.\n        self.food_rating_map[food] = newRating\n        # Insert the '(new rating, name)' element in the respective cuisine's priority queue.\n        cuisineName = self.food_cuisine_map[food]\n        heapq.heappush(self.cuisine_food_map[cuisineName], Food(newRating, food))\n\n    def highestRated(self, cuisine: str) -> str:\n        # Get the highest rated 'food' of 'cuisine'.\n        highest_rated = self.cuisine_food_map[cuisine][0]\n\n        # If the latest rating of 'food' doesn't match with the 'rating' on which it was sorted in the priority queue,\n        # then we discard this element from the priority queue.\n        while self.food_rating_map[highest_rated.food_name] != highest_rated.food_rating:\n            heapq.heappop(self.cuisine_food_map[cuisine])\n            highest_rated = self.cuisine_food_map[cuisine][0]\n\n        # Return the name of the highest-rated 'food' of 'cuisine'.\n        return highest_rated.food_name", "title": "Design a Food Rating System", "url": "/submissions/detail/1121678346/", "lang_name": "Python3", "time": "1\u00a0month, 2\u00a0weeks", "timestamp": 1702804177, "status": 10, "runtime": "801 ms", "is_pending": "Not Pending", "memory": "49.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Food:
    def __init__(self, food_rating, food_name):
        # Store the food's rating.
        self.food_rating = food_rating
        # Store the food's name.
        self.food_name = food_name

    def __lt__(self, other):
        # Overload the less than operator for comparison.
        # If food ratings are the same, sort based on their name (lexicographically smaller name food will be on top).
        if self.food_rating == other.food_rating:
            return self.food_name < other.food_name
        # Sort based on food rating (bigger rating food will be on top).
        return self.food_rating > other.food_rating


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map food with its rating.
        self.food_rating_map = {}
        # Map food with the cuisine it belongs to.
        self.food_cuisine_map = {}
        # Store all food of a cuisine in a priority queue (to sort them on ratings/name).
        # Priority queue element -> Food: (food_rating, food_name)
        self.cuisine_food_map = defaultdict(list)

        for i in range(len(foods)):
            # Store 'rating' and 'cuisine' of the current 'food' in 'food_rating_map' and 'food_cuisine_map' maps.
            self.food_rating_map[foods[i]] = ratings[i]
            self.food_cuisine_map[foods[i]] = cuisines[i]
            # Insert the '(rating, name)' element into the current cuisine's priority queue.
            heapq.heappush(
                self.cuisine_food_map[cuisines[i]], Food(ratings[i], foods[i])
            )

    def changeRating(self, food: str, newRating: int) -> None:
        # Update food's rating in 'food_rating' map.
        self.food_rating_map[food] = newRating
        # Insert the '(new rating, name)' element in the respective cuisine's priority queue.
        cuisineName = self.food_cuisine_map[food]
        heapq.heappush(self.cuisine_food_map[cuisineName], Food(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the highest rated 'food' of 'cuisine'.
        highest_rated = self.cuisine_food_map[cuisine][0]

        # If the latest rating of 'food' doesn't match with the 'rating' on which it was sorted in the priority queue,
        # then we discard this element from the priority queue.
        while (
            self.food_rating_map[highest_rated.food_name] != highest_rated.food_rating
        ):
            heapq.heappop(self.cuisine_food_map[cuisine])
            highest_rated = self.cuisine_food_map[cuisine][0]

        # Return the name of the highest-rated 'food' of 'cuisine'.
        return highest_rated.food_name
