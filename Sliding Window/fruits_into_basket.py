# https://leetcode.com/problems/fruit-into-baskets
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 
# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].


def fruits_into_baskets(fruits):
	if len(fruits) <= 2:
		return len(fruits)
	
	basket = dict()
	window_start = 0
	longest_so_far = 0

	for window_end, fruit in enumerate(fruits):
		basket[fruit] = basket.get(fruit, 0) + 1

		while len(basket) > 2:
			window_start_fruit = fruits[window_start]
			basket[window_start_fruit] -= 1

			if basket[window_start_fruit] == 0:
				del basket[window_start_fruit]
				
			window_start += 1
		
		longest_so_far = max(longest_so_far, window_end-window_start+1)
	
	return longest_so_far