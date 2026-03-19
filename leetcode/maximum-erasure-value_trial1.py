class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans=nums[0]
        sums=ans
        win = set([nums[0]])
        right=1
        left=0
        while right<len(nums):
            if nums[right] in win:
                while nums[right] in win:
                     win.remove(nums[left])
                     ans -= nums[left]
                     left += 1
                ans+=nums[right]
                win.add(nums[right])
                sums=max(sums,ans)
            else:
                ans+=nums[right]
                win.add(nums[right])
                sums=max(sums,ans)
            right+=1
        return sums
                

        