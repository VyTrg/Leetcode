class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_res = int(0)
        check_set = set()
        low = int(0)
        for high in range(len(s)):
            while s[high] in check_set:
                check_set.remove(s[low])
                low += 1
            check_set.add(s[high])
            max_res = max(max_res, high - low + 1)
        return max_res

