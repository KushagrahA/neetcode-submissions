class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        for n in nums:
            res *= n
        return [res // n for n in nums]