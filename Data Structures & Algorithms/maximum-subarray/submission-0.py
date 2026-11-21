class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        highest_sum = nums[0]

        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            highest_sum = max(curr_sum, highest_sum)
        return highest_sum