'''Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
'''




def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left ,right = 0, len(height)-1
    maxwatercontainer = 0
    while left<right:
        width = right - left
        if height[left] < height[right]:
            min_height = height[left]
            left += 1
        else:
            min_height = height[right]
            right -= 1
                
        maxwatercontainer = max(maxwatercontainer, width*min_height)
    return maxwatercontainer

print (maxArea([1,2,1]))