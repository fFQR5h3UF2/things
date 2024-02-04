# Submission for 01 Matrix
# Submission url: https://leetcode.com/submissions/detail/1023967521/


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_count = len(mat)
        column_count = len(mat[0])
        max_distance = row_count + column_count + 1
        invalid_rows, invalid_columns = (-1, row_count), (-1, column_count)

        distances = [[-1] * column_count for _ in range(row_count)]
        deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(row_count):
            for column in range(column_count):
                if mat[row][column] != 0:
                    continue

                distances[row][column] = 0
                for delta_row, delta_column in deltas:
                    new_row, new_column = row + delta_row, column + delta_column
                    if new_row in invalid_rows or new_column in invalid_columns:
                        continue

                    if (
                        mat[new_row][new_column] == 1
                        and distances[new_row][new_column] == -1
                    ):
                        distances[new_row][new_column] = 1

        def get_distance(row: int, column: int) -> int:
            if row in invalid_rows or column in invalid_columns:
                return max_distance

            calculated = distances[row][column]
            if calculated != -1:
                return calculated

            min_distance = max_distance

            for delta_row, delta_column in deltas:
                new_distance = 1 + get_distance(row + delta_row, column + delta_column)
                if new_distance < min_distance:
                    min_distance = new_distance

            distances[row][column] = min_distance
            return min_distance

        for row in range(row_count):
            for column in range(column_count):
                if distances[row][column] != -1:
                    continue

                get_distance(row, column)

        return distances
