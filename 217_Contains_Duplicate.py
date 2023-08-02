class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort(reverse = False)
        for i in range(0, n - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False