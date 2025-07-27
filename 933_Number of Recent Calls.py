from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Freq = Counter(arr)
        print(Freq)
        occurence = list(Freq.values())
        if len(occurence) == len(set(occurence)):
            return True 
        else:
            return False

        