# Time Complexity: O(n²) - Because we have 2 Loops
# Space Complexity: O(1) - I store just 2 simple variables

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for pointer1 in range(len(nums)):
            pointer2 = pointer1 + 1

            while pointer2 < len(nums):
                if nums[pointer1] + nums[pointer2] == target:
                    return [pointer1, pointer2]

                pointer2 += 1 

        return []