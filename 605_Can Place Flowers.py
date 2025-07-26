class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0

        for i in range(length):
            if flowerbed[i] ==0:
                left_clear = (i==0) or (flowerbed[i-1]==0) 
                right_clear =(i==length -1) or (flowerbed[i+1]==0)

                if left_clear and right_clear:
                    flowerbed[i]=1
                    count+=1
               
        return count>=n
        