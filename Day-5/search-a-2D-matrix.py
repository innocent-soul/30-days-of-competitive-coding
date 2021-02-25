class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # linear approach.  :v
        # see constraints before applying applying Binary Searches.
        # matrix size is maximum 100 X 100  even O(mn) will easily work  :D
        for row in matrix:
            if target <= row[-1]:
                return target in row 
            
        return False 
