# second attempt with char array Solved everything
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        charArray = [0] * 26
        for i in range(len(s)):
            charArray[ord(s[i])- ord('a')] = charArray[ord(s[i])- ord('a')]+1
        for i in range(len(t)):
            charArray[ord(t[i])- ord('a')] = charArray[ord(t[i])- ord('a')]-1
        for i in range(26):
            if charArray[i] !=0:
                return False
        return True
