class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ans=[]
        zeros=[]
        nots=[]
        for i in nums:
            if i==0:
                zeros.append(i)
            else:
                nots.append(i)
        ans=nots+zeros
        for  i in range(len(nums)):
            nums[i]=ans[i]


        