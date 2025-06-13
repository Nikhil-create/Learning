from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(open: int, close: int, s: str):
            if len(s) == 2*n:
                res.append(s)
                return 
            if open < n:
                helper(open + 1, close, s= s+ "(")
            if close < open:
                helper(open, close + 1, s= s+")")
        res = []
        helper(0,0,"")
        return res

        