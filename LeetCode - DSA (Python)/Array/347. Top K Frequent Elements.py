from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        res,ans = [],[]
        for num,feq in counter.items():
            heapq.heappush(res,(-1*feq,num))

        while k>0:
            n = heapq.heappop(res)
            ans.append(n[1])
            k-=1