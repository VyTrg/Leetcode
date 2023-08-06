class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = False)
        res = int(sys.maxsize)
        n = len(nums)
        for i in range(k - 1, n):
            res = min(res, nums[i] - nums[i - k + 1])

        return res        
        