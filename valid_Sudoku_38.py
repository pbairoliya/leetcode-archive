"""
PsuedoCode

-Everytime you go through a number in the board, add it as a row stirng tag
col string tag and box tag it is in
- After the array is fully made with all tag convert it to a set and see if the
len changes if it does then not an actual good sodoku - cuz it should be the same

"""
class Solution(object):
    def isValidSudoku(self, board):
        
        sodukoTag =[]
        for i in range(len(board)):
            for j in range(len(board[i])):
                sodukoElement = board[i][j]
                if sodukoElement!='.':
                    sodukoTag.append("row" + str(i) + str(sodukoElement))
                    sodukoTag.append("col" + str(j) + str(sodukoElement))
                    sodukoTag.append("box" + str(i/3) + str(j/3) + str(sodukoElement))
        #sets will remove mulitple instances
        setSodukoTag = set(sodukoTag)

        #checks if both lengths are the same thus Tag is same length as set meaning no duplicates
        if len(sodukoTag) != len(setSodukoTag):
            return False
        
        else:
            return True
