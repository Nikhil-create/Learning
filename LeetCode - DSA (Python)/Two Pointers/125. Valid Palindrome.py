class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c.lower())

        left = 0
        right = len(strs) -1

        while left < right:
            if strs[left] != strs[right]:
                return False
            left +=1
            right -=1
        return True