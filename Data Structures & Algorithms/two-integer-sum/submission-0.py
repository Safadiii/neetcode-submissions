class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for (index, value) in enumerate(nums):
            if target-value in values.keys():
                return sorted([index, values.get(target-value)])
            else:
                values[value] = index