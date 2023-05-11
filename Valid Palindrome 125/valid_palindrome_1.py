"""
Pseudocode
remove all non alphanumeric parts of stirng and set input string to updated string
have two pointers one from start and the second from the end and meet each otehr in the middle
if it loops to middle and each character at pointer the same then return true else false 
"""

class Solution(object):
    def isPalindrome(self, s):
        # make the string remove all spaces and non alpah numeric cahracters
        s = ''.join(s.split()).lower()
        s = ''.join(c for c in s if c.isalnum())

        # our two pointers
        i = 0 
        j = len(s)-1
        if len(s) == 0 or len(s) == 1:
            return True
        
        while i<j and i<len(s) and j>=0:
            if s[i] == s[j]:
                i +=1
                j -=1
            else:
                return False
        
        return True