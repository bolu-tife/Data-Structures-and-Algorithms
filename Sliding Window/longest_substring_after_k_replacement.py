# https://leetcode.com/problems/longest-repeating-character-replacement/
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


def longest_substring_after_k_replacement(string, k):
    window_start = 0
    max_frequency = 0
    char_count = dict()
    longest_so_far = 0

    for window_end, char in enumerate(string):
        char_count[char] = char_count.get(char, 0) + 1

        # The reason for keeping a maximum frequency is to know the number of extra characters asides the most occuring in the current window size
        max_frequency = max(max_frequency, char_count[char])

        #to reduce the window size when the current size has more than k extra characters asides from the most occuring character
        if window_end-window_start + 1 - max_frequency > k: 
            start_value = string[window_start]
            char_count[start_value] -= 1
            window_start += 1

        longest_so_far = max(longest_so_far, window_end-window_start+1)

    return longest_so_far

      

assert longest_substring_after_k_replacement(string="aabccbb", k=2) == 5
assert longest_substring_after_k_replacement(string="abbcb", k=1) == 4
assert longest_substring_after_k_replacement(string="abccde", k=1) == 3

# Time Complexity: O(n)
# Space Complexity: O(26) => O(1) because we have atmost 26 uppercase english letters and the space remains the same as it grows 
# n is the total size of the array

# It's best to visualize the solution to understand it.
