#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for cnt in count.values():
            if cnt > 1:
                return True
        return False
      
solution = Solution()
