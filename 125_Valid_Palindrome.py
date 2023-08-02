class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s:
            result = []
            for i in s.lower():
                if i.isalnum():
                    result.append(i)
            return result == result[::-1]
        else:
            return False