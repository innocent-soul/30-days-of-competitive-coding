'''
availiable of geeksforgeeks.

THIS CODE GIVES TIME LIMIT EXCEED 

BUT THIS IS CLEARLY O(N)  !!!!

..cries in python  :'v

'''


class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr, n):
		ans = [] 
		
		i = 0
		while i < n - 1:
		    x = i
		    while i < n - 1 and arr[i] < arr[i + 1]:  # increasing
		        i += 1 
		       
		    ans.append((x, i))
		    
		    while i < n - 1 and arr[i] > arr[i + 1]:  # decreasing
		        i += 1
		 
	    return ans 


## Their 'inbuilt code' (code that I can't change seems preety time consuming to me.  :|
