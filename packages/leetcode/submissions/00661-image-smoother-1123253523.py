# Submission title: for Image Smoother
# Submission url  : https://leetcode.com/submissions/detail/1123253523/
# Submission json : {"id": 1123253523, "status_display": "Accepted", "lang": "python3", "question_id": 661, "title_slug": "image-smoother", "code": "class Solution:\n    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:\n        # Save the dimensions of the image.\n        m = len(img)\n        n = len(img[0])\n\n        # Create a new image of the same dimension as the input image.\n        smooth_img = [[0] * n for _ in range(m)]\n\n        # Iterate over the cells of the image.\n        for i in range(m):\n            for j in range(n):\n                # Initialize the sum and count \n                sum = 0\n                count = 0\n\n                # Iterate over all plausible nine indices.\n                for x in (i - 1, i, i + 1):\n                    for y in (j - 1, j, j + 1):\n                        # If the indices form valid neighbor\n                        if 0 <= x < m and 0 <= y < n:\n                            sum += img[x][y]\n                            count += 1\n\n                # Store the rounded down value in smooth_img[i][j].\n                smooth_img[i][j] = sum // count\n        \n        # Return the smooth image.\n        return smooth_img", "title": "Image Smoother", "url": "/submissions/detail/1123253523/", "lang_name": "Python3", "time": "1\u00a0month, 2\u00a0weeks", "timestamp": 1702974287, "status": 10, "runtime": "463 ms", "is_pending": "Not Pending", "memory": "17.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Create a new image of the same dimension as the input image.
        smooth_img = [[0] * n for _ in range(m)]

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the sum and count
                sum = 0
                count = 0

                # Iterate over all plausible nine indices.
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        # If the indices form valid neighbor
                        if 0 <= x < m and 0 <= y < n:
                            sum += img[x][y]
                            count += 1

                # Store the rounded down value in smooth_img[i][j].
                smooth_img[i][j] = sum // count

        # Return the smooth image.
        return smooth_img
