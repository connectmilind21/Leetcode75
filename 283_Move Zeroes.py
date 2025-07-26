class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_list = [0]*length
        index = 0

        for i in range (length):
            if nums[i]!=0:
                zero_list[index] = nums[i]
                index+=1
        for i in range (length):
            nums[i]=zero_list[i]
        