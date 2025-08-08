class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(i, curString):
            # If we reached the length of digits, we found a combination
            if len(curString) == len(digits):
                res.append(curString)
                return
            
            # Loop over all letters that the current digit can represent
            for c in phone_map[digits[i]]:
                backtrack(i + 1, curString + c)      # Explore
            
        backtrack(0, "")
        return res
