# first attempt tried using a dictionary and seeing if the other value that needs
#to be there to make the target sum
class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        i = 0
        for num in nums:
            numMap[num] = i
            i =i+1
        for counter in range(len(nums)):
            firstNum = nums[counter]
            secondNum = target-firstNum
            print(secondNum)
            if secondNum in numMap:
                if numMap[firstNum] != numMap[secondNum]:
                    return [numMap[firstNum], numMap[secondNum]]
