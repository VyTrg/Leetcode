class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt = int(0)
        n = len(s)
        for i in range(1, n - 1):
            if(s[i - 1] != s[i] and s[i] != s[i + 1] and s[i - 1] != s[i + 1]):
                cnt = cnt + 1
        return cnt