class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s = "babad"
        max_start, max_end = 0, 0
        
        for i in range(len(s)):
            # 홀수
            start, end = i, i
            
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if (max_end - max_start) < (end - start):
                    max_start = start
                    max_end = end
                start = start-1
                end = end+1 
                
            # 짝수
            start, end = i, i+1
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if (max_end - max_start) < (end - start):
                    max_start = start
                    max_end = end
                start = start-1
                end = end+1 
                            
        return s[max_start:max_end+1]
        