def longest_substring_with_distinct_characters(string):
    if len(string) <= 1:
        return len(string)

    char_seen = set()
    longest_so_far = 0
    window_start = 0

    for window_end, char in  enumerate(string):
        while char in char_seen:
            win_start_elem = string[window_start]
            char_seen.remove(win_start_elem)
            window_start += 1

        char_seen.add(char)
        longest_so_far = max(longest_so_far, window_end-window_start+1)

    return longest_so_far

assert longest_substring_with_distinct_characters("aabccbb") == 3
assert longest_substring_with_distinct_characters("abbbb") == 2
assert longest_substring_with_distinct_characters("abccde") == 3

# Time Complexity: O(n)
# Space Complexity: O(n) 
# n is the total size of the array
