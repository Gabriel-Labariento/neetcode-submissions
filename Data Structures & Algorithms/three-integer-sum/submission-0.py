class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        res = []

        for i in range(len(nums)):
            if sn[i] > 0:
                break
            
            if i > 0 and sn[i] == sn[i - 1]:
                continue
             
            j, k = i + 1, len(nums) - 1
            while j < k:
                tsum = sn[i] + sn[j] + sn[k]
                if tsum < 0:
                    j += 1
                elif tsum > 0:
                    k -= 1 
                else:
                    res.append([sn[i], sn[j], sn[k]])
                    j += 1
                    k -= 1
                    while sn[j] == sn[j - 1] and j < k:
                        j += 1
        return res

        
