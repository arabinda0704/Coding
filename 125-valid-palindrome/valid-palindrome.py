class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        s1 = list(s)  # modified line to make s1 mutable
        l, r = 0, len(s1) - 1
        while l < r:
            temp = s1[l]
            s1[l] = s1[r]
            s1[r] = temp
            r -= 1
            l += 1
        if s1 == list(s):
            return True
        return False