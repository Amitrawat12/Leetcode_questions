class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        # for s in words:
        #     i =0
        #     j = len(s)-1
        #     flag = False
        #     if j ==0:
        #         return s
        #     while i<(len(s)//2):
        #         if s[i] == s[j]:
        #             flag = True 
        #         else:
        #             flag = False
        #             break
        #         i+=1
        #         j-=1
        #     if flag == True:
        #         return s
        # return ""
        for word in words:
            if word == word[::-1]:
                return word
        return ""