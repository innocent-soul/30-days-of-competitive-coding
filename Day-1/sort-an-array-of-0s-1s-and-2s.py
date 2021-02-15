'''
given an array of size N contaning only 0s, 1s, and 2s;
sort the array in ascending order  INPLACE.

Expected Time Complexity:  O(N)
Expected Auxiliary Space:  O(1)
'''

def sort012(arr):
    # ummm... how about this..
    numbers = [0, 0, 0]  # represents number of 0, number of 1 and number of 2 in arr
    for n in arr:
        numbers[n] += 1

    ## it doesn't change the original array AND ALSO USES EXTRA SPACE :
    ## arr = [0] * numbers[0] + [1] * numbers[1] + [2] * numbers[2]

    # So, let's do this:

    # for i in range(len(arr)):  # wait.. maybe, range(N) uses N space.  :v
    # So,
    i = 0
    while i < len(arr):
        if numbers[0] > 0:
            arr[i] = 0
            numbers[0] -= 1
        elif numbers[1] > 0:
            arr[i] = 1
            numbers[1] -= 1
        else:  # if numbers[2] > 0
            arr[i] = 2
            numbers[2] > 0

        # and a very nasty line:
        i += 1


'''
# test case
z = [0, 2, 1, 2, 0]
sort012(z)
print(z)
'''
