from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        st = []

        for i in range(len(temperatures)):
            while st and temperatures[i] > temperatures[st[-1]]:
                index = st.pop()
                output[index] = i - index
            st.append(i)
        return output
        