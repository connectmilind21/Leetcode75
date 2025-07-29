class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n

        left_product = 1
        for i in range (n):
            result[i] = left_product
            left_product*= nums[i]
          
        right_product = 1
        for i in reversed (range (n)):
            result[i] *= right_product
            right_product*= nums[i]

        
        return result