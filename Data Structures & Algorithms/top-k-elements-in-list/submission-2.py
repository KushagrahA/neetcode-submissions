class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        for i in range(k):
            num = max(freq, key=freq.get)  # key with highest count
            res.append(num)
            del freq[num]                  # so it isn't picked again
        return res