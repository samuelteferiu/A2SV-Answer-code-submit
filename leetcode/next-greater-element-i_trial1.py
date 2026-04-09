class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        dicts={}
        out=[]
        for i in reversed(nums2):
            while stack:
                if stack[-1]>i:
                    dicts[i]=stack[-1]
                    stack.append(i)
                    break
                else:
                    stack.pop()
            if not stack:
                dicts[i]=-1
                stack.append(i)
        for j in nums1:
            out.append(dicts[j])
        return out        