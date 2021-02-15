'''
given an unsorted array arr if size N of positive integers.
one number 'A' from set {1, 2, ....N} is missing and
one number 'B' occurs twice in array.
Find these two numbers.

Expected Time Complexity:  O(N)
Expected Auxiliary Space:  O(1)
'''


# Let me explain the whole approach for you.  :)
def findTwoElement(arr):
    # Hmm..  I had two failed attempts.
    # First, I tried finding sum of arr  and 'expected sum'  (sum of numbers from 1 to N)
    # Then I attached a 'weight' to each element..  ( it seemed promising though.  :v )

    # I had two failed attempts.  But.. I got a right approach via combining these 2.  :)

    # Consider, that value of missing element is x and repeated element is y.
    # Also, refer 'expected array' to be {1, 2, ....N}
    # So, expected array   = { 1, 2, .. , x, .. y, ....N }
    # And given array, arr = { 1, 2, .. , y, .. y, ....N }

    # Subtracting these, we get:  x - y = expected_sum - sum_of_arr

    # Now, attach a weight of 'n' on element n.  i.e., umm.. just square all numbers.  :v

    # So,  x**2 - y** 2 = expected_sum_of_sq - sum_of_sq_of_arr
    #      (x + y) * (x - y) = ...


    ## oof.. I really spent too much time on this.  :'v

    # sum_of_arr = sum(arr)  # am I allowed to use this  ??  :v
    sum_of_arr = 0
    for n in arr:
        sum_of_arr += n

    N = len(arr)
    expected_sum = (N * (N + 1)) // 2

    x_minus_y = expected_sum - sum_of_arr


    sum_of_sq_of_arr = 0
    for n in arr:
        sum_of_sq_of_arr += n * n

    expected_sum_of_sq = ( N * (N + 1) * (2*N + 1) ) // 6

    x_plus_y =  (expected_sum_of_sq - sum_of_sq_of_arr) // x_minus_y

    # return y, x
    return (x_plus_y - x_minus_y) // 2, (x_plus_y + x_minus_y) // 2


'''
# test case:
z = [1, 3, 3]
## z = [1, 2, 3, 7, 5, 6, 7, 8, 9, 10]
print(*findTwoElement(z))
# Expected Output:  3, 2
'''
