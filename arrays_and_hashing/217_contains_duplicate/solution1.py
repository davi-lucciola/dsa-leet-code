# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_already_seem = set()

        for num in nums:
            if num in nums_already_seem:
                return True
            
            nums_already_seem.add(num)

        return False