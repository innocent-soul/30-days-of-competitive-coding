'''
Given a collection of Intervals, the task is to merge all of the overlapping Intervals.

Example 1:

Input:
N = 4
Intervals = {(1,3),(2,4),(6,8),(9,10)}
Output: 1 4 6 8 9 10
Explanation: Given intervals: [1,3],[2,4]
[6,8],[9,10], we have only two overlapping
intervals here,[1,3] and [2,4]. Therefore
we will merge these two and return [1,4],
[6,8], [9,10].


Expected Time Complexity: O(N*Log(N) ).
Expected Auxiliary Space: O(1).
'''

def overlappedInterval(Intervals,n):
    # sorry for taking advantage of python.  :p
    ## I didn't imported anything though.  :v
    
    Intervals.sort()  #  :D
    
    min_, max_ = Intervals[0]
    
    i = 0
    while i < n - 1:
        if Intervals[i + 1][0] <= max_:
            max_ = max(max_, Intervals[i + 1][1])
            i += 1
        else:
            yield min_, max_
            min_, max_ = Intervals[i + 1]
            i += 1
            
    
    yield min_, max_
