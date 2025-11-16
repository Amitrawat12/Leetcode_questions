class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        c = []
        d =[]
        while i< n:
            c.append(nums[i])
            i+=1
            c.append(nums[j])
            j+=1
        return c