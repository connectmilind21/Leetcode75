class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum= current_sum
        length = len(nums)

        for i in range(k, length):
            current_sum = current_sum-nums[i-k]+nums[i]
            max_sum = max(current_sum, max_sum)
    
        return max_sum/k

        