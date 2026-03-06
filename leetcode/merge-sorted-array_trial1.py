class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m==0 or n==0:
            if m==0:
                nums1[:n]=nums2[:n]
                return nums1
            if n==0:
                return nums1
        else:
            l=m-1
            r=n-1
            last=m+n-1
            while l>=0 and r >=0:
                if nums1[l]>nums2[r]:
                    nums1[last]=nums1[l]
                    l-=1
                else:
                    nums1[last]=nums2[r]
                    r-=1
                last-=1
            if r >= 0:
                nums1[:r + 1] = nums2[:r + 1]
            return nums1

            

        