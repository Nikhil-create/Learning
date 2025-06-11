from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sumOfNum = numbers[left] + numbers[right]

            if sumOfNum == target:
                return [left +1, right+1]
            elif sumOfNum > target:
                right -=1
            else:
                left +=1