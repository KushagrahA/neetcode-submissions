class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = 1
        for i in nums:
            res = res*(i+1)
        for i in nums:
            nums[i] = res/(nums[i])
        return nums
        