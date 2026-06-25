from collections import defaultdict
class Solution:
    def giveDict(self, s: str) -> dict:
        dic = defaultdict(int)
        for i in s:
            dic[i] += 1
        return dic

    def compareDict(self, S: dict, T: dict) -> bool:
        return S == T

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            S = self.giveDict(s)
            T = self.giveDict(t)
            if self.compareDict(S,T):
                return True
            else:
                return False
        