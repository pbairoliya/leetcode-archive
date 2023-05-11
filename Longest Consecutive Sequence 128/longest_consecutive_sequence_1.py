"""
PseudoCode
If the nums array lenght is either 0 or 1 its longest consecutive is already 0 or 1
respectivley

- make a set of all sorted nubmers this will show the longest iteration
- count the longest subset from this set and thus you have longest string
"""


class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        sortedNumsSet = sorted(set(sorted(nums)))
        print(sorted(nums))
        sortedNums = list(sortedNumsSet)
        lengthCounter = 1
        lenMax =  1 
        currMax = 1
        print(sortedNums)
        for i in range(1, len(sortedNums)):
            if sortedNums[i] - sortedNums[i-1] == 1:
                lengthCounter +=1
            else:
                lengthCounter =1
            if currMax <= lengthCounter:
                currMax = lengthCounter
        if lenMax < currMax:
            lenMax = currMax
        return lenMax