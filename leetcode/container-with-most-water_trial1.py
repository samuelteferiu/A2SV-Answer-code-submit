class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxs=0
        while l<r:
            left=height[l]
            right=height[r]
            mins=min(left,right)
            base= r-l
            areas=mins*base
            maxs=max(maxs,areas)
            if left<right:
                l+=1
            else:
                r-=1
        return maxs



        