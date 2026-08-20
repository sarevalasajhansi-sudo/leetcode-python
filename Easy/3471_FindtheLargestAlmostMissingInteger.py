class Solution(object):
    def largestInteger(self, nums, k):
        count = {}

        for i in range(len(nums) - k + 1):
            subarray = set(nums[i:i + k])

            for x in subarray:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x in count:
            if count[x] == 1:
                ans = max(ans, x)

        return ans