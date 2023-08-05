class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = int(0)
        res = int()
        n = len(nums)
        for i in range(0, k):
            sum += nums[i]
        res = sum
        for i in range(k, n):
            sum = sum + nums[i] - nums[i - k]
            if (sum > res):
                res = sum
        return res/k