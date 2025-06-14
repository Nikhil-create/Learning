from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,v] for p,v in zip(position,speed)]
        st = []

        for p,v in sorted(pairs, reverse=True):
            st.append((target-p)/v)
            if len(st) > 1 and st[-1] <= st[-2]:
                st.pop()
                
        return len(st)