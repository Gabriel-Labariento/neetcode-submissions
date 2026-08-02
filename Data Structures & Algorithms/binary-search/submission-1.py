class Solution:
    def binary_search(self, l, r, nums, target):
        mid = (l + r) // 2

        if l > r:
            return -1

        if target == nums[mid]:
            return mid

        if target < nums[mid]:
            return self.binary_search(l, mid - 1, nums, target)

        else:
            return self.binary_search(mid + 1, r, nums, target)
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
        
        
