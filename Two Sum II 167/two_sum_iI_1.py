"""
Pseudocode
Have two pointers one starting from 0, one from the end and see if the sum of pointers
is the target if it is less than move the left pointer forward, and if greater than the 
right target left this can be done cuz the array is alr sorted
"""
class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1

        while i<j:

            if numbers[i]+ numbers[j] == target:
                return [i+1,j+1]
            if numbers[i] + numbers[j] < target:
                i +=1
            else:
                j -=1