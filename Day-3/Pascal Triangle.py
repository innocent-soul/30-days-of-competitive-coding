'''
Given a positive integer N, return the Nth row of pascal's triangle.  modulo 10**9 + 7

Expected Time Complexity: O(N**2)
Expected Auxiliary Space: O(N**2)

However, I 'kindaa' did it in O(N) time and O(1) space complexity.  :3
'''

def nthRowOfPascalTriangle(self,n):
	    n -= 1
	    prev_term = 1
	    yield prev_term 
	    for r in range(n):
	        prev_term = ( (prev_term * (n - r)) // (r + 1) ) # % 1000000007   ## Don't try modulo while dividing.  :'v
	        yield prev_term % 1000000007  # pretty big numbers.  :'v
