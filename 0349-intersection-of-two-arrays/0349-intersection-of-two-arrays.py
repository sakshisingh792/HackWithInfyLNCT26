class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        seen=set()
        for i in range(min(n1,n2)):
            if n1<n2:
                if nums1[i] in nums2:
                    seen.add(nums1[i])
            else:
                if nums2[i] in nums1:
                    seen.add(nums2[i])

        return list(seen)                    


        