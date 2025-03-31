class Solution:
    

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(output,i,j):
            while i<j:
                temp = output[i]
                output[i]= output[j]
                output[j]=temp
                i+=1
                j-=1
            return output
        
        k = k%len(nums)
        
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)


            