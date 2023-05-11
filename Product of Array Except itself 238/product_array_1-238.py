#this code works for 19/22 test cases dont know what to do when there are multiple zeros
#doesnt do left and right mulitpliaction 
class Solution(object):
    def productExceptSelf(self, nums):
        answer = [0] * len(nums)
        product = nums[0]
        nonzeroProd = nums[0]
        for i in range(1,len(nums)):
            product = product * nums[i]
            if nums[i] !=0:
                nonzeroProd = nonzeroProd*nums[i]
    
        for i in range(len(nums)):
            if nums[i] !=0:
                answer[i] = product / nums[i]
            else:
                answer[i] = nonzeroProd
        
        return answer
        