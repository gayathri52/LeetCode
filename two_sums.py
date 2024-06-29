#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in num_to_index:
                return [num_to_index[diff], ind]
            num_to_index[val] = ind
