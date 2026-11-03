class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = []
        for i in range(len(strs)):
            c[i] = Counter(i)
        for i in range(len(strs)):
            for j in range(len(strs)):
                if c[i] == c[j]:
                    list.add(c[i], c[j])
                    