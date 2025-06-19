class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        print(words)
        return " ".join(words[::-1])