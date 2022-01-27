# https://leetcode.com/problems/letter-combinations-of-a-phone-number/


# BFS approach


def letterCombinations( digits):
    if digits == "":
        return []

    alphanum = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}

    queue = [""]
    index = 0
    while queue:
        size = len(queue)
        for i in range(size):
            curr = queue.pop(0)
            for char in alphanum[digits[index]]:
                
                queue.append(curr + char)
        if index == len(digits) -1:
                return queue
        index += 1
    

# print(letterCombinations("2"))
# print(letterCombinations("23"))
# print(letterCombinations("234"))
# print(letterCombinations("222"))


# DFS approach

def letterCombo(digits):
    if not digits:
        return []

    mappings = {"2": "abc", "3": "def", "4": "ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9":"wxyz"}
    output = list()
    letterComboHelper(digits, "", 0, output, mappings)

    return output

def letterComboHelper(digits, current, index, output, mappings):
    if len(current) == len(digits):
        output.append(current)
    
        return
    
    for char in mappings[digits[index]]:
        letterComboHelper(digits, current + char, index+1, output, mappings)

print(letterCombo("2"))
print(letterCombo("23"))
print(letterCombo("234"))
print(letterCombo("222"))