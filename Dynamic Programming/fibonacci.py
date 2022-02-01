# https://leetcode.com/problemsc
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:
# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


# Brute-Force Approach
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Top-Down (with Memoization) Approach
# using hashmaps
def fibonacci_top_down(n):
    if n < 2:
        return n
    return fibonacci_memo(n, {})

def fibonacci_memo(n, memo):
    if n < 2:
        return n
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)

    return memo[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# using arrays
def fibonacci_top_down_array(n):
    if n < 2:
        return n
    dp = [float('-inf') for i in range(n+1)]
    return fibonacci_memo_array(n, dp)

def fibonacci_memo_array(n, memo):
    if n < 2:
        return n
    if memo[n] != float('-inf'):
        return memo[n]

    memo[n] = fibonacci_memo_array(n-1, memo) + fibonacci_memo_array(n-2, memo)

    return memo[n]

# Time Complexity: O(n)
# Space Complexity: O(n)

# Buttom-Up (Tabulation) Approach
def fibonacci_buttom_up(n):
    if n < 2:
        return n
    dp = [0 for i in range(n+1)]
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Time Complexity: O(n)
# Space Complexity: O(n)


# without using extra space
def fibonacci_buttom_up(n):
    if n < 2:
        return n
    first = 0
    second = 1

    for i in range(2,n+1):
        temp = first + second
        first = second
        second = temp

    return second

# Time Complexity: O(n)
# Space Complexity: O(1)