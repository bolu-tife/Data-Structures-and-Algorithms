# https://leetcode.com/problems/container-with-most-water/submissions/


def maxArea( height) :
    
    maxarea = float("-inf")
    start = 0
    end = len(height)-1
    
    while start <= end:
        left = height[start]
        right = height[end]
        maxarea = max(maxarea, (end-start)*(min(left, right )))
        
        if left < right:
            start +=1
        else:
            end -=1
                        
    return maxarea
    
    
    
        
        # bruteforce
        
#         maxarea = float("-inf")
        
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 left = height[i]
#                 right = height[j]
                
#                 maxarea = max(maxarea, min(left,right) * (j-i))
                
#         return maxarea