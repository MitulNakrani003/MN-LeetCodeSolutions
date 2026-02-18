class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totaln = len(nums1) + len(nums2)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        half = (m+n+1)//2
        lo, hi = 0, m

        while lo <= hi:
            mid1 = (hi+lo)//2
            mid2 = half-mid1

            l1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')

            r1 = nums1[mid1] if mid1 < m else float('inf')
            r2 = nums2[mid2] if mid2 < n else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                hi = mid1 - 1
            else:
                lo = mid1 + 1
        return 0