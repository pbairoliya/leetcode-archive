# My solution solved first try no help needed
class Solution(object):
    def containsDuplicate(self, nums):
        numDup = set()
        for x in nums:
            if x in numDup:
                return True

            else:
                numDup.add(x)
        return False