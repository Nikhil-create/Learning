class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        return len(set(nums)) != len(nums)

