class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} #value: index

        for i,n in enumerate(nums):
            diff = target - n
            if n in map:
                return [map[diff], i]
            map[n] = i
        return 