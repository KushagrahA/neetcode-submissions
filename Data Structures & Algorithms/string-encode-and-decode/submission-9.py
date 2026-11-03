class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= len(s) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 
        while i < len(str):
            j = i
            while j != "#":
                    length 
        return res