class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenth = 0
        start, end = 0, 0
        
        char = set()
        while(end < len(s)):
            # print(s[start], s[end], char)
            if s[end] in char:
                char.remove(s[start])
                start += 1
                
            else:
                char.add(s[end])
                max_lenth = max(end - start + 1,max_lenth)
                end += 1
                
        return max_lenth
                
                

            
            
            
            