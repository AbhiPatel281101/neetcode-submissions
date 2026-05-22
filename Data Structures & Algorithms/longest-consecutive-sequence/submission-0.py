class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert to a set for O(1) lookups
        numSet = set(nums)
        longest = 0 

        for n in nums:
            # Only start a sequence if 'n' is the beginning of one
            if (n - 1) not in numSet:
                length = 1
                # Expand the sequence as long as the next number exists
                while (n + length) in numSet:
                    length += 1
                
                # Update the global maximum
                longest = max(length, longest)
                
        return longest