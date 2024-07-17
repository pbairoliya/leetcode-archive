class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0 
        #loop through right
        for right in range(len(nums)):
            #when found something that isnt 0
            if nums[right] != 0:
                #swap
                nums[left],nums[right] = nums[right],nums[left]
                left +=1
        