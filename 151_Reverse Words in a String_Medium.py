class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.strip().split()
        return ' '.join(reversed(word))