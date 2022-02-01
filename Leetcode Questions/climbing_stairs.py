# class Solution:
    
#     def climbStairs(self, n: int) -> int:
        # using dynamic programming without array
        # time complexity: O(n)
        # space complexity: O(1)
#         if n < 3:
#             return n
#         first = 1
#         second = 2
#         for i in range(n-2):
#             temp = first + second
#             first = second
#             second = temp
            
#         return second
    
    
    # using dynamic programming with array
        # time complexity: O(n)
        # space complexity: O(n)
#         if n < 3:
#             return n
#         partial_arr = [1,2]
        
#         for i in range(n-2):
#             partial_arr.append(partial_arr[-1]+ partial_arr[-2]) 
            
#         return partial_arr[-1]
        
        
        
    # using recursion and memoization  
    # time complexity: O(n)
    # space complexity: O(n)
    
#     def climbStairs(self, n: int) -> int:
        
#         return self.climber(n, {})
    
#     def climber(self, n, memo):
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         if n in memo:
#             return memo[n]
        
#         memo[n] = self.climber(n-1, memo) + self.climber(n-2, memo)
        
#         return memo[n]


# using just recursion
    # time complexity: O(n^2)
    # space complexity: O(n)
#     def climbStairs(self, n: int) -> int:
        
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
        
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
        
