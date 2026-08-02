class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0
        curr_length = 0
        last = None

        for num in nums:
            if num - 1 not in nums_set:
                last = num
                curr_length = 1
                while last + 1 in nums_set:
                    curr_length += 1
                    last += 1
            if curr_length > longest:
                longest = curr_length
        return longest