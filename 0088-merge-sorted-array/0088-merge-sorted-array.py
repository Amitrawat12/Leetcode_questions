class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,m+n):
            if nums1[i] == 0:
                nums1[i] = nums2[i-m]
        nums1.sort()

        