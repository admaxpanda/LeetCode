# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while(r-l>1):
            if(isBadVersion(version=(r+l)//2)):
                r=(r+l)//2
            else:
                l=(r+l)//2
        if(r==l):
            return r
        else:
            if(isBadVersion(version=l)):
                return l
            return r