class Solution:
        def isPalindrome(self, s: str) -> bool:
                Newstr = ''
                for c in s:
                        if c.isalnum():
                                Newstr += c.lower()
                return  Newstr == Newstr[::-1]
                
