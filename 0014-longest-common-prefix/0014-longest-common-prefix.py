class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        v=sorted(strs)
        first=v[0]
        last=v[-1]
        for i in range(len(first)):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 
        