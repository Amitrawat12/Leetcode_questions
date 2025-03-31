class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        i = 0 
        j = 0
        while i<len(nums):
            if nums[i]%2!=0:
                i+=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
                i+=1
        return nums