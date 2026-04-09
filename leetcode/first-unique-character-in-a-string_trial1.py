class Solution:
    def firstUniqChar(self, s: str) -> int:
        test=Counter(s)
        ans=0
        for ind,i in enumerate(s):
            if test[i]==1:
                ans=ind
                return ans
        return -1
                
        