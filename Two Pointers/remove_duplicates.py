def remove_duplicates(arr):
  # TODO: Write your code here
  if len(arr) <2 :
    return len(arr)
  non_duplicate = 0
  for runner in range(1,len(arr)):
    if arr[non_duplicate] != arr[runner]:
      non_duplicate += 1
      arr[non_duplicate] = arr[runner]
  return non_duplicate + 1


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number of element in the array 