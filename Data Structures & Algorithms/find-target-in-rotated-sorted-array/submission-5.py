class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        # First pass, we try to find the cut
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        cut = l

        # Second pass, we use the cut to search two arrays, for the target
        l, r = 0, len(nums) - 1

        if target >= nums[cut] and target <= nums[r]: 
            l = cut
        else:
            r = cut - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                # Search left
                r = mid - 1
            else:
                # Search right
                l = mid + 1
        return -1