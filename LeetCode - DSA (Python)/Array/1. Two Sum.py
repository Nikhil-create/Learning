class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hash_map = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash_map:
                return [hash_map[comp],i]
            hash_map[nums[i]] = i