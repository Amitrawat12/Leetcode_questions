class Solution:
    def reverseWords(self, s: str) -> str:
        d = s.split()
        c=[]
        for i in d:
            c.append(i[::-1])
        e = " ".join(c)
        return e