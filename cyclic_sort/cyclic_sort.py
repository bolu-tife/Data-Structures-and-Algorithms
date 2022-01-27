# My code

def cyclic_sort(nums):
  # TODO: Write your code here
  i = 0
  while i < len(nums):
    
    while i != nums[i]-1:
      temp = nums[i]-1
      nums[i], nums[temp] = nums[temp], nums[i]
    i += 1
  return nums

# Educative soln

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1
  return nums


def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()


# [3, 1, 5, 12, 2, 11], K = 4
# 1,2,3,5,6,11,12

# Welcome to the chat room!
# BroadcasterSpleadly: https://cvcompiler.com
# edem_gold1: ,😂😂🤣
# BroadcasterSpleadly: Sign up for early access of Spire: http://getspire.io/
# spacebeamer98: 🔥🔥🔥
# edem_gold1: 🌱
# BroadcasterSpleadly: Connect with Ewere: https://www.linkedin.com/in/ewerechukwu-asaka/
# BroadcasterSpleadly: Connect with Luke: https://www.linkedin.com/in/luke-ndatigh/
# BroadcasterSpleadly: Connect with Chukwuka: https://www.linkedin.com/in/chukwuka-ezeoke/
# BroadcasterSpleadly: Connect with Ofure: https://www.linkedin.com/in/ofure-ughu/
# BroadcasterSpleadly: Connect with Tochukwu: https://www.linkedin.com/in/tochukwu-nkemdilim/
# ogechukwu97: 🤙
# Welcome to the chat room!
