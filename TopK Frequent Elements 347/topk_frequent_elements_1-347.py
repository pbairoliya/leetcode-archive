"""
PsuedoCode
1)make a map of all the frequncies of each new number 2)sort the map based off frequency 3) print the top k elemnts using a for loop
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        solList = []

        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] =  freqMap[num]+1
            else:
                freqMap[num] = 1
   
        sortedFreList = [key for key, val in sorted(freqMap.items(), key = lambda item: -item[1])]
        print(sortedFreList)
        for i in range(k):
            solList.append(sortedFreList[i])
        
        return solList

