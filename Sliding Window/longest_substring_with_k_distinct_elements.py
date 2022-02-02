# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

# Example 3:
# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

# Example 4:
# Input: String="cbbebi", K=10
# Output: 6
# Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".


def find_longest_substring_k_distinct(string, k):
    if k == 0:
        return 0
    if k > len(string):
        return len(string)

    char_count = dict()
    window_start  = 0
    longest_so_far = 0

    for window_end, char in enumerate(string):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k and window_start <= window_end:
            current_start = string[window_start]
            if char_count[current_start] == 1:
                del char_count[current_start]
            else:
                char_count[current_start] -= 1
            window_start += 1

        longest_so_far = max(longest_so_far, window_end-window_start+1)

    return longest_so_far


assert find_longest_substring_k_distinct("araaci", 2) == 4
assert find_longest_substring_k_distinct("araaci", 1) == 2
assert find_longest_substring_k_distinct("cbbebi", 3) == 5
assert find_longest_substring_k_distinct("araaci", 10) == 6

# Time Complexity: O(n)
# Space Complexity: O(k) 
# n is the total size of the array