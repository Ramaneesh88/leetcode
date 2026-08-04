class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w=s.split()
        a=w[-1]
        b=len(a)
        return b
        