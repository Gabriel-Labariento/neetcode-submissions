class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_prods = [1]
        suffix_prods = [1]
        last = 1
        
        products = []

        for i in range(len(nums) - 1):
            p_prod = last * nums[i]
            last = p_prod
            prefix_prods.append(last)

        last = 1
        for j in range(len(nums) - 1, 0, -1):
            s_prod = last * nums[j]
            last = s_prod
            suffix_prods.insert(0, last)
        
        for k in range(len(nums)):
            products.append(prefix_prods[k] * suffix_prods[k])

        return products