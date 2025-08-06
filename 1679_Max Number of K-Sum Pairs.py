from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter()
        operation = 0

        for num in nums:
            target = k -num
            if count[target]>0:
                operation+=1
                count[target]-=1
            else:
                count[num]+=1
        return operation
        
        