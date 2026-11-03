class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)

        hashset = set()
        for i in range(len(nums)):
            if (nums[i]== nums[i+1]):
                i+=1
            if (nums[i] + 1 == nums[i+1]):
                hashset.add(nums[i])
            
        return len(hashset)