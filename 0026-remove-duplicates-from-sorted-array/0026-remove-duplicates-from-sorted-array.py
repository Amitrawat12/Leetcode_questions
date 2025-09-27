class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        prev = nums[0]
        count = 1
        for i in range(len(nums)):
            if nums[i]!=prev:
                prev = nums[i]
                count = count +1
                nums[i],nums[slow] = nums[slow],nums[i]
                slow+=1
        return count
            