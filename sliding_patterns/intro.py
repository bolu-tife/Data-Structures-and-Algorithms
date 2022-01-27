# Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

# Normal approach - brute force O(n * k)
# edge cases 
# if k > len(arr): empty list
# if empty arr? empty list

def normal(arr, k):
    
    if not arr:
        return []
    output = list()

    for i in range(len(arr)-k+1): # 9- 5 = 4 + 1 = 5 O(N)s
        temp = 0
        for j in range(i, i+k): #O(K)
            temp += arr[j]
        output.append(temp/k)

    return output

print(normal([1, 3, 2, 6, -1, 4, 1, 8, 2],5))
print(normal([2,3,4],5))



