class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = ''.join(c.lower() for c in s if c.isalnum())
        second = first[::-1]

        return first == second