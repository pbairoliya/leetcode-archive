#using a sliding windo in theory, doing a prefix mulitplicaiton before the index
#and setting the result array to prefix multiplication, then calculating a postfix
#product and mulitplying it to answer array which gets us everyting but the index in
#multiplication!, and sends out that reusltant answer array

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix =1
        for i in range(len(nums)-1,-1,-1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer

        