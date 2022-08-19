class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_arr = n * [0]
        r_arr = n * [0]
        
        result = 0
        max_left_val = 0
        max_right_val = 0
        
        for i in range(0, n):
            if max_left_val <= height[i]:
                l_arr[i] = height[i]
                max_left_val = height[i]
            else:
                l_arr[i] = max_left_val
                
                
        for i in range(n-1, -1,-1):
            if max_right_val <= height[i]:
                r_arr[i] = height[i]
                max_right_val = height[i]
            else:
                r_arr[i] = max_right_val
                
        for i in range(0, n):
            if min(l_arr[i], r_arr[i]) > height[i]:
                result += min(l_arr[i], r_arr[i]) - height[i]
        
        return result
            
