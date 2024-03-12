class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        '''
        Problem: need to recursively backtrack through the gridand add curr letter to string
        #Choice, does adding the letter make a substring of the word
        base case: index out of bounds or already visited
        recursive case: recursively build the string from that point by going either horizontal or vertical
        return if the word == word
        '''

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def createWords(row, col, i):
            if i == len(word):
                return True
            if(row < 0 or col < 0 or row >= ROWS or col >= COLS or word[i] != board[row][col] or (row, col) in visited):
                return False
            
            visited.add((row, col))
            result = (createWords(row, col + 1, i + 1) or createWords(row, col - 1, i + 1) or createWords(row + 1, col, i + 1) or createWords(row - 1, col, i + 1))
            visited.remove((row, col))
            return result
        
        for i in range(ROWS):
            for j in range(COLS):
                if createWords(i, j, 0):
                    return True
        return False
        