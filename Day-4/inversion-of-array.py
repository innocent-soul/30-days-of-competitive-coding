''' 
availiable of geeksforgeeks.com 
Given an array of integers. Find the Inversion Count in the array. 

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).
'''

#User function Template for python3

# arr[]: Input Array
# N : Size of the Array arr[]

def merge_sort(arr):
    global ans 
    
    if len(arr) > 1:
        mid = len(arr) >> 1
        
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1 
            else:
                arr[k] = R[j]
                ans += mid - i
                j += 1 
            k += 1
            
        
        while i < len(L):
            arr[k] = L[i]
            i += 1 
            k += 1
            
        
        while j < len(R):
            arr[k] = R[j] 
            j += 1 
            k += 1
            
        

ans = 0    
    
def inversionCount(arr,n):
    global ans
    ans = 0
    
    merge_sort(arr)
    # print(arr)
    return ans 
