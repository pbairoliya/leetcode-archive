#second attempt this time isntead of needing two for loops use enumerate that lists
#index and values in that array - we can use both same map logic too.
class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        for index, currentNum in enumerate(nums):
            secondNum = target-currentNum
            if secondNum in numMap:
                index2 = numMap[secondNum]
                return [index,index2]
            else:
                numMap[currentNum] = index
