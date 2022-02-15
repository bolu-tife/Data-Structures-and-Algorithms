def is_happy_number(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    slow = square(num)
    fast = square(square(num))
    while fast != slow:
        slow = square(slow)
        fast = square(square(fast))

        if slow == fast:
            break

    return slow == 1



def square(num):
    square_sum = 0
    while num:
        rem = num % 10
        square_sum += rem ** 2

        num //=10
    
    return square_sum

assert is_happy_number(23)
assert is_happy_number(100)
assert not is_happy_number(12)


#   Time complexity = O(n)
#   Space complexity = O(1)
# where n is the number