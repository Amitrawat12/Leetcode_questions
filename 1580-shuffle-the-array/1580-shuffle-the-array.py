class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        c = []
        while i< n:
            c.append(nums[i])
            c.append(nums[i+n])
            i+=1
        return c