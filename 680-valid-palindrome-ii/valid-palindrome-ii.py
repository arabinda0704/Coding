def is_palindrome(s,l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(s,l + 1, r) or 
                        is_palindrome(s,l, r - 1))
            l += 1
            r -= 1

        return True