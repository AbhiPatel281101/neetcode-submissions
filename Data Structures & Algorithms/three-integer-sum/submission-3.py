class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # 1. Corrected from .short()
        
        for i, a in enumerate(nums):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # 2. Start 'l' at i + 1 to only look forward
            l, r = i + 1, len(nums) - 1 
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for the left pointer
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res