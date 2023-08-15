class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0
        str_num = str(num)
        n = len(str_num)
        i = 0
        j = k
        while(j <= n):
            if(int(str_num[i:j]) > 0):
                if(num % int(str_num[i:j]) == 0):
                    cnt += 1
            i += 1
            j += 1
        return cnt