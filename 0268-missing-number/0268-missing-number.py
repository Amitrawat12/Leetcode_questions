class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum =0
        for i in range(len(nums)+1):
            sum+=i
        find =sum
        for i in range(len(nums)):
            find-=nums[i]
        return find