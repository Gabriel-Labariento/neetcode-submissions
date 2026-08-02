class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        res = []

        for i, n in enumerate(nums):
            
            if n in hm:
                res.append(hm.get(n))
                res.append(i)
                return res

            diff = target - n
            if diff not in hm:
                hm[diff] = i
