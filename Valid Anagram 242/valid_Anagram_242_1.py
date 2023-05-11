# First Attempt using two sets and comparing them
class Solution(object):
    def isAnagram(self, s, t):
        sL = len(s)
        tL = len(t)
        if sL != tL:
            return False
        sSet = set()
        tSet = set()

        for char in s:
            sSet.add(char)
        for char in t:
            tSet.add(char)

        for val in sSet:
            if val not in tSet:
                return False
            
        return True
