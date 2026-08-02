class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        sn = set(nums)

        return len(sn) != len(nums)


