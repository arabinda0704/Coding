
def alphaNum(c):
    return (65 <= ord(c) <= 90 or 
            97 <= ord(c) <= 122 or 
            48 <= ord(c) <= 57)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not alphaNum(s[l]):
                l += 1
            while r > l and not alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    