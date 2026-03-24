class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        res=0
        crsum=0
        prefix={0:-1}
        for i in range(0,len(nums)):
            crsum+=nums[i]
            div=crsum%k
            if div in prefix:
                if (i - prefix[div]) >= 2:
                    return True
            else:
                prefix[div]=i
            
        return False