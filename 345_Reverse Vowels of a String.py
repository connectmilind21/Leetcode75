class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vovels = set('aeiouAEIOU')
        left=0
        right = len(s)-1

        while left < right:
            while left < right and s[left] not in vovels:
                left+=1
            while left < right and s[right] not in vovels:
                right-=1
            
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return ''.join(s)
            