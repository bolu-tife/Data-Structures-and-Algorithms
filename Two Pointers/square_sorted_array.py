def square_sorted(arr):
    left = 0
    right = len(arr)-1

    squares = [0 for i in arr]
    square_index = len(arr)-1
    while left < right:
        left_sqr = arr[left] * arr[left] 
        right_sqr = arr[right] * arr[right]

        if left_sqr < right_sqr:
            squares[square_index] = right_sqr
            right -= 1
        else:
            squares[square_index] = left_sqr
            left += 1
        square_index -=1
    
    return squares
    
print(square_sorted([-2, -1, 0, 2, 3]))
print(square_sorted([-3, -1, 0, 1, 2])) 

            
#   Time complexity = O(n)
#   Space complexity = O(n)
# where n is the number of element in the array 