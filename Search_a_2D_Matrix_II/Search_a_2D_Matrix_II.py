class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        # for i in range(len(matrix)):
        #     if matrix[i][0]>target:
        #         return False
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j]==target:
        #             return True
        #         if matrix[i][j]>target:
        #             break
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height-1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else: # found it
                return True
            
        return False