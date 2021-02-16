'''
Given an array arr of N integers. 
Find the contiguous sub-array with maximum sum.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

def maxSubArraySum(a,size):
    # umm.. How about this..
    
    for i in range(size - 1):
        a[i + 1] = max(a[i + 1], a[i] + a[i + 1])
    
    return max(a)
