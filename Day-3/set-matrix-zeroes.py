''' 
set-matrix-zeroes   availiable on leetcode

I did this question on another day though..  
I didn't had a leetcode account 
..and after making it, I forgot about this series and did some random (but nice) question.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False 
        first_col_zero = False
        
        
        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                if elem == 0:   
                    if i == 0:
                        first_row_zero = True
                        if j == 0:
                            first_col_zero = True   # At this point, I wanna read books named 'clean code' and 'complete code'.  
                            # ..because, it still didn't give corrent answer due to a silly mistake.  :'v
                    elif j == 0:
                        first_col_zero = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    
        
        for row_no in range(1, len(matrix)):
            if matrix[row_no][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[row_no][j] = 0

        for col_no in range(len(matrix[0])):
            if matrix[0][col_no] == 0:
                for i in range(len(matrix)):
                    matrix[i][col_no] = 0
        
        if first_row_zero:
            # first row should be all zero 
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
            
        
