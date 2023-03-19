#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        for i in range(len(s)//2):
            if(s[i]!=s[len(s)-i-1]):
                return 0
        return 1
# @lc code=end

