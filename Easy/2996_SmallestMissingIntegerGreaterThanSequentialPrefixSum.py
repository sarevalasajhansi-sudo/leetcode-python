class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]

        # Find the longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest missing integer >= total
        x = total
        while x in nums:
            x += 1

        return x