"""
Pseudocode
have a left and right pointer have a maxVol var that keeps track of each
volume created 

if the height of the right pointer is greater then incriment left by one seeing if that vol is more
else move right towards 0
"""
class Solution(object):
    def maxArea(self, height):
        left = 0 
        right = len(height) -1
        maxVol = 0
        while right > left:
            lowerHeight = min(height[left], height[right])
            vol = (right-left)*lowerHeight
            if maxVol< vol:
                maxVol = vol
            if height[right] > height[left]:
                left +=1
            else:
                right -=1
        return maxVol