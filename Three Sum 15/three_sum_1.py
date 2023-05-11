"""
Pseudocode
sort the array 
loop through the elements of the array and create a left pointer which is one greater
than the index of element and one from the right and see if it adds to 0, if greater 
make right go less and if it is too less incriment the left 

"""

class Solution(object):
    def threeSum(self, nums):
        solList = set()
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while k>j and j<len(nums)-1:
                threeSum = nums[i]+nums[j]+nums[k]
                if threeSum == 0:
                    validSol = [nums[i],nums[j],nums[k]]
                    solList.add(tuple(validSol))
                    k-=1
                elif threeSum > 0:
                    k-=1
                else:
                    j+=1

        return solList