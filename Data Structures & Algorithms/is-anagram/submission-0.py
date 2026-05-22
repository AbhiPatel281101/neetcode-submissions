class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
obj = Solution()
s = "racecar"
t = "carrace"
print(obj.isAnagram(s,t))