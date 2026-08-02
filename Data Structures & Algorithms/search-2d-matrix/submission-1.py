class Solution:
    def binary_search(self, nums, target):
        mid = len(nums) // 2

        if len(nums) < 1:
            return False

        if nums[mid] == target:
            return True

        elif target < nums[mid]:
            return self.binary_search(nums[:mid], target)

        else:
            return self.binary_search(nums[mid + 1:], target)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix) - 1 and matrix[row][-1] < target:
            row += 1
        
        if row > len(matrix) - 1:
            return False

        nums = matrix[row]
        return self.binary_search(nums, target)
