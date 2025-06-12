class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {'}':'{',')':'(',']':'['}
        st = []
        for c in s:
            if c in hash_map.values():
                st.append(c)
            else:
                if not st or st.pop() != hash_map[c]:
                    return False
                    
        return True if not st else False
