'''
availiable on geeksforgeeks.com 

Given a square matrix of size N x N. 
The task is to rotate it by 90 degrees in anti-clockwise direction without using any extra space. 

Expected Time Complexity: O(N**2)
Expected Auxiliary Space: O(1)
'''


def rotateby90(arr, n):
    # print(*arr, sep = '\n')
    for i in range((n + 1) >> 1):
        for j in range(i, n - i - 1):
            x = arr[i][j] 
            for _ in range(4):
                i, j = n - j - 1, i
                arr[i][j], x = x, arr[i][j]
                
            
