class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height = {}
        for i in range(len(heights)):
            height[heights[i]] =names[i]
        
        heights.sort(reverse = True)
        l =[]
        for i in heights:
            l.append(height[i])
        
        return l

        