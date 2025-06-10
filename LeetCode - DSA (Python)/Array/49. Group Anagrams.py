from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            idx = "".join(sorted(s))
            res[idx].append(s)

        return list(res.values())