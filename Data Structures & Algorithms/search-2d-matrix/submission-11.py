class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search splitting the matrix for each search
        midpoint = len(matrix)//2
        right_idx = len(matrix) - 1
        left_idx = 0
        if matrix is None:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        if len(matrix) == 1:
            if target in matrix[0]:
                return True
            else:
                return False
        while left_idx <= right_idx:
            midpoint = (left_idx + right_idx) //2

            if matrix[midpoint][0] <= target <= matrix[midpoint][-1]:
                if target in matrix[midpoint]:
                    return True
                else:
                    return False
            elif target <= matrix[midpoint][-1]:
                right_idx = midpoint - 1
            else:
                left_idx = midpoint + 1
        return False
